from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin
from core.models import GoogleBotVisit, NormalVisit
import ipaddress
import socket
from functools import lru_cache


@lru_cache(maxsize=5000)
def reverse_dns_check(ip):
    """Return hostname for given IP, cached for performance."""
    try:
        hostname, _, _ = socket.gethostbyaddr(ip)
        return hostname
    except Exception:
        return None


GOOGLEBOT_IP_RANGES = [
    "8.8.4.0/24",
    "8.8.8.0/24",
    "8.34.208.0/20",
    "8.34.208.0/23",
    "8.34.210.0/24",
    "8.34.211.0/24",

    # IPv6 ranges
    "2001:4860:4801:1a::/64", "2001:4860:4801:1b::/64", "2001:4860:4801:1c::/64",
    "2001:4860:4801:1d::/64", "2001:4860:4801:1e::/64", "2001:4860:4801:1f::/64",
    "2001:4860:4801:2a::/64", "2001:4860:4801:2b::/64", "2001:4860:4801:2c::/64",
    "2001:4860:4801:2d::/64", "2001:4860:4801:2e::/64", "2001:4860:4801:2f::/64"
]


def is_ip_in_google_ranges(ip):
    """Check if an IP is within Googlebot ranges."""
    try:
        ip_obj = ipaddress.ip_address(ip)
        for cidr in GOOGLEBOT_IP_RANGES:
            if ip_obj in ipaddress.ip_network(cidr):
                return True
    except ValueError:
        pass
    return False


class GoogleBotRedirectMiddleware(MiddlewareMixin):
    def process_request(self, request):
        user_agent = request.META.get("HTTP_USER_AGENT", "").lower()
        ip = (
            request.META.get("HTTP_X_FORWARDED_FOR", "").split(",")[0]
            or request.META.get("REMOTE_ADDR", "unknown")
        )
        path = request.path

        # --- Identify bots or unknowns ---
        is_googlebot = "googlebot" in user_agent
        is_unknown = (
            not user_agent
            or user_agent.strip() == ""
            or user_agent == "unknown"
            or any(x in user_agent for x in ["bot", "crawler", "spider", "headlesschrome"])
        )
        verified_google_ip = is_ip_in_google_ranges(ip)
        reverse_dns = reverse_dns_check(ip)

        is_google_host = (
            reverse_dns
            and any(reverse_dns.endswith(x) for x in [
                ".googlebot.com",
                ".googleusercontent.com",
                ".google.com",
            ])
        )
        is_unknown_host = reverse_dns is None
        print("DEBUG:", ip, user_agent, reverse_dns, {
    "googlebot": is_googlebot,
    "unknown_user_agent": is_unknown,
    "google_ip": verified_google_ip,
    "google_host": is_google_host,
    "unknown_host": is_unknown_host,
})
        # --- ✅ Redirect bots/unknown ONLY if visiting home ("/") ---
        if path == "/" and (is_googlebot or is_unknown or verified_google_ip or is_google_host or is_unknown_host):
            if ip != "49.47.71.252":
                GoogleBotVisit.objects.create(
                    ip_address=ip,
                    user_agent=request.META.get("HTTP_USER_AGENT", ""),
                    path_accessed=path,
                    verified_google_ip=verified_google_ip,
                )
            return redirect("/about/")

        # --- CASE 2: Normal human visitor ---
        elif ip != "49.47.71.252":
            NormalVisit.objects.create(
                ip_address=ip,
                user_agent=request.META.get("HTTP_USER_AGENT", ""),
                path_accessed=path,
            )

        return None
