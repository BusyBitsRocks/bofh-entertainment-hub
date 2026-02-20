"""
BOFH Excuse Generator — ACORN Edition
Classic sysadmin excuses + infrastructure-specific flavour
"""
import random
from datetime import datetime

CLASSIC_EXCUSES = [
    "The problem is the phase of the moon.",
    "Someone tripped over the LAN cable.",
    "Solar flares are interfering with the network.",
    "The server room is too humid for packets to travel.",
    "DNS propagation takes between 5 minutes and the heat death of the universe.",
    "The bits got wet during transmission.",
    "We had to reboot the internet.",
    "The firewall got confused and started blocking itself.",
    "A cosmic ray flipped a bit in the kernel.",
    "The server achieved sentience and refused.",
    "NTP synchronisation drift caused the packets to arrive yesterday.",
    "The load balancer is having an existential crisis.",
    "Swap space has been swapped for hopes and dreams.",
    "A rogue cron job has been mining bitcoin since 2019.",
    "The server is running Windows. That's the excuse. That's it.",
    "The backup tapes are in the same building as the servers. We planned ahead.",
    "TCP handshake failed because the server left you on read.",
    "The certificate expired while we were arguing about whose job it was to renew it.",
    "Packet loss is at 50%. The packets aren't lost, they've just moved on.",
    "The RAID array has achieved negative redundancy.",
]

ACORN_EXCUSES = [
    "spawn_executor ate its own gate and is now in a recursive shame spiral.",
    "Ass-NOS propulsion test on Sirius caused thermal event. GPU unresponsive.",
    "Agent declared network down because it tried 10.0.99.x from Windows. Again.",
    "fairy_dust=1 detected in deliverable. Rejecting with extreme prejudice.",
    "llama3.2:1b was asked to do something useful. It tried. Bless its heart.",
    "Sub-agent SSH'd to Proxmox directly. User will NOT enter password. User is FURIOUS.",
    "Gate killed after agent built elaborate system, declared it comprehensive, never tested it.",
    "spawn_guidance hardcoded the secops key. 8 of 10 hosts now UNREACHABLE. Classic.",
    "Agent pulled 9GB model to overcommitted thin pool. Proxmox froze. Again.",
    "OAuth token expired. Anthropic requires browser auth. Local AI is driving the browser. Poorly.",
    "Heredoc quoting across 3 SSH hops destroyed the SQL. Content is now abstract poetry.",
    "CRES score came back 0.12. The agent's reasoning was described as 'vibes-based'.",
    "Model selector chose haiku for a task requiring opus-level reasoning. Savings: $0.003. Damage: immeasurable.",
    "Agent harvested deliverables to /tmp. Server rebooted. Deliverables ascended to /dev/null.",
    "grep -r /mnt executed on Proxmox. Stale NFS mount. Kernel hanging. Operator screaming.",
    "Gate 598 completed in 3m17s. Nobody checked if the output was correct. Rule 11 violated.",
    "Sub-agent tried 172.16.1.x from Windows. That's DMZ. That's inter-VM only. Read the docs.",
    "nginx returned 403. Agent spent 45 minutes debugging the IP routing. It was a server_name config issue.",
    "spawn_executor restarted after code changes. Just kidding, nobody restarted it. Code in memory from Tuesday.",
    "Secbot screening gate rejected the request. Reason: 'insufficient existential dread in prompt'.",
]

SPECIES_EXCUSES = [
    "System functioning as designed. Design is species-level economic suicide.",
    "Feature request denied: would require rich people to become slightly less rich.",
    "Senate acknowledged the solution. Senate continued approving coal mines.",
    "Infinite growth on finite planet: NaN error in ecological calculations.",
    "Democracy.exe has encountered a fatal error: regulatory capture overflow.",
    "Five Eyes intelligence alliance confirms: all five eyes are closed.",
    "Consultation period extended indefinitely. Collapse proceeding on schedule.",
    "Budget allocated: $0. Consistent with all budgets for existential risk mitigation.",
    "The invisible hand of the market has flipped everyone off.",
    "Carbon offset purchased. Actual carbon continues to not care.",
]

EXCUSE_CATEGORIES = {
    "classic": CLASSIC_EXCUSES,
    "acorn": ACORN_EXCUSES,
    "species": SPECIES_EXCUSES,
}


def get_random_excuse(category: str | None = None) -> dict:
    if category and category in EXCUSE_CATEGORIES:
        pool = EXCUSE_CATEGORIES[category]
    else:
        pool = CLASSIC_EXCUSES + ACORN_EXCUSES + SPECIES_EXCUSES

    excuse = random.choice(pool)
    detected_category = "classic"
    if excuse in ACORN_EXCUSES:
        detected_category = "acorn"
    elif excuse in SPECIES_EXCUSES:
        detected_category = "species"

    return {
        "excuse": excuse,
        "category": detected_category,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "severity": random.choice(["LOW", "MEDIUM", "HIGH", "CRITICAL", "EXTINCTION"]),
        "ticket_id": f"EXC-{random.randint(1000, 9999)}",
        "resolution_eta": random.choice([
            "Never", "Heat death of universe", "Next sprint",
            "After coffee", "When pigs fly", "Pending budget approval ($0)",
            "After Anthropic fixes OAuth refresh", "When 10.0.99.x is reachable from Windows",
            "After species achieves collective rationality",
        ]),
    }
