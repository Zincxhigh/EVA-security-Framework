# EVA-Security Framework

The EVA is a dual-component cybersecurity interface designed to monitor, manage, and visualize network security events. Built as the visual frontend and dedicated hardware display for the EVA-security-Framework firewall backend, this project combines a hardware-accelerated desktop application with a custom-engineered USB OLED monitor.

The entire system features a strict Evangelion-inspired aesthetic utilizing high-contrast red-on-black wireframes, sharp geometry and terminal-style readouts.

# The Custom Firewall System

### Firewall contents

- [x] Firewall hardware or software — the device/system that enforces the rules.

- [x] Network interfaces — connections to the Internet/WAN, LAN, DMZ, etc.

- [x] Rule set / access-control policies — specifies which traffic is allowed or blocked.

- [ ] Stateful inspection — tracks active connections and their states.

- [ ] NAT (Network Address Translation) — translates private and public IP addresses when needed.

- [x] Logging and monitoring — records allowed, blocked, and suspicious traffic.

- [ ] Authentication/identity controls — can restrict access based on users or devices.

- [ ] VPN support — provides encrypted remote or site-to-site connections.

- [ ] Intrusion detection/prevention (IDS/IPS) — identifies and potentially blocks malicious traffic.

- [ ] Configuration and management interface — used by administrators to configure the firewall.

- [ ] Updates/signatures — keeps threat-detection rules and software current.

### Privicy Enforcement Layer Contents

 - [ ] API protection
  
 - [ ] Fingerprint ctrl
        
 - [ ] Data policies
        
 - [ ] Tracker blocking

 - [ ] DNS filtering
       
 - [ ] Cookie/storage
          
 - [ ] Permission ctrl
         
 - [ ] Profile manager
       
 - [ ] Audit/logging


### IPS Privicy layer on top of Firewall from stopping website tracking systems

                                                 ┌──────────────────────┐
                                                 │       Browser        │
                                                 └──────────┬───────────┘
                                                            │
                                               ┌──────────────────────────┐
                                               │    Privacy Enforcement   │
                                               │          Layer           │
                                               └────────────┬─────────────┘
                                                            │
                                                 ┌──────────▼───────────┐
                                                 │ Windows Firewall/WFP │
                                                 └──────────┬───────────┘
                                                            │
                                                         Internet




