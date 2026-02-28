# 🛡️ Cyber-Learning Roadmap
### Offensive Security & IoT Penetration Testing — Python to OSCP

> A structured, stage-by-stage path from zero to OSCP and beyond.  
> Every stage builds on the last. Don't skip. Don't rush. Be consistent.

---

## 📋 Table of Contents

- [Stage 1 — Python + Linux Foundations](#stage-1--python--linux-foundations)
- [Stage 2 — Networking](#stage-2--networking)
- [Stage 3 — Security Fundamentals](#stage-3--security-fundamentals)
- [Stage 4 — Penetration Testing Basics](#stage-4--penetration-testing-basics)
- [Stage 5 — Web Application Security](#stage-5--web-application-security)
- [Stage 6 — Practical Pentesting](#stage-6--practical-pentesting)
- [Stage 7 — First Certification (eJPT)](#stage-7--first-certification-ejpt)
- [Stage 8 — Active Directory + OSCP Prep](#stage-8--active-directory--oscp-prep)
- [Stage 9 — IoT Hacking Begins](#stage-9--iot-hacking-begins)
- [Stage 10 — Advanced IoT](#stage-10--advanced-iot)
- [Stage 11 — Final Goal (OSCP)](#stage-11--final-goal-oscp)

---

## Stage 1 — Python + Linux Foundations

> Run Python and Bandit **simultaneously** — don't wait for one to finish before starting the other. Set up your lab environment during this stage.

### 🐍 Python
- [ ] **100 Days of Code** — Angela Yu (Udemy)
  - Complete all 100 days fully
  - Build every project, don't skip exercises
  - Focus especially on: loops, functions, file I/O, OOP, APIs, and automation scripts

### 🐧 Linux
- [ ] **OverTheWire: Bandit** — [overthewire.org/wargames/bandit](https://overthewire.org/wargames/bandit)
  - Complete all 34 levels
  - Start from Level 0 — no shortcuts
  - Document every command and trick you learn

### 🖥️ Lab Setup
- [ ] Download and install **VirtualBox**
- [ ] Download **Kali Linux** ISO and set up as a VM
- [ ] Get comfortable with the Kali desktop, terminal, and basic tools
- [ ] Take a snapshot of your clean Kali install before touching anything

### ✅ Stage 1 Complete When:
- All 100 Python days done
- All 34 Bandit levels completed
- Kali VM is running and usable

---

## Stage 2 — Networking

> Understand how data moves. This is the foundation of every attack and defense you'll ever study.

### 📚 Courses
- [ ] **Jason Dion — CompTIA Network+ (N10-009)** (Udemy) ✅ *Already purchased*
- [ ] **Professor Messer — Network+** (Free) — [professormesser.com](https://www.professormesser.com)
  - Use both in parallel — Dion for depth, Messer for clarity

### 🛠️ Hands-On Practice (in Kali VM)
- [ ] **Wireshark** — capture and analyze real traffic
- [ ] **Nmap** — scan your local network, understand flags and output
- [ ] **Netcat** — basic listeners, banners, file transfers

### 🧪 Labs
- [ ] **TryHackMe** — "Network Fundamentals" rooms (after finishing courses)

### ✅ Stage 2 Complete When:
- Both Network+ courses finished
- Comfortable using Wireshark, Nmap, Netcat from the terminal
- TryHackMe Network Fundamentals rooms done

---

## Stage 3 — Security Fundamentals

> Learn how defenders think. You need this to understand what you're trying to break.

### 📚 Courses
- [ ] **Jason Dion — CompTIA Security+ (SY0-701)** (Udemy) ✅ *Already purchased*
- [ ] **Professor Messer — Security+** (Free) — [professormesser.com](https://www.professormesser.com)

### 🧪 Labs
- [ ] **TryHackMe** — "Pre-Security" path (after finishing courses)

### ✅ Stage 3 Complete When:
- Both Security+ courses finished
- TryHackMe Pre-Security path completed

---

## Stage 4 — Penetration Testing Basics

> First real offensive training. Every room gets a proper write-up.

### 🧪 Labs
- [ ] **TryHackMe** — "Jr Penetration Tester" path
  - Complete every room in order
  - Don't jump ahead

### 📝 Lab Reporting (Start Here)
- [ ] Write a basic lab report for **every room**
- [ ] Publish all reports to this GitHub repo under `/Reports/Stage4/`
- [ ] Use a consistent format: Target, Methodology, Findings, Tools Used, Lessons Learned

### ✅ Stage 4 Complete When:
- All Jr Penetration Tester rooms completed
- Reports written and published for every room

---

## Stage 5 — Web Application Security

> Every IoT device has a web interface. Every OSCP exam has web targets. This stage is non-negotiable.

### 📚 Platform
- [ ] **PortSwigger Web Security Academy** (100% Free) — [portswigger.net/web-security](https://portswigger.net/web-security)
  - Complete **every lab** in every topic, in order
  - Don't skip topics — SQLi, XSS, SSRF, XXE, authentication, access control, etc.
  - Use Burp Suite Community for all labs

### 🎯 Why This Stage Matters
- Fixes the biggest gap in most pentesting roadmaps
- Directly prepares for OSCP web targets
- IoT devices almost always have a web admin panel — this is how you get in

### ✅ Stage 5 Complete When:
- All PortSwigger labs completed across all topics
- Comfortable using Burp Suite for web testing

---

## Stage 6 — Practical Pentesting

> Hands-on. No passive watching. Every technique gets replicated.

### 📚 Course
- [ ] **TCM Security — Practical Ethical Hacking** (Udemy)
  - Watch and **immediately replicate** every technique in your Kali VM
  - Don't just watch — pause, set up the environment, do it yourself

### 🧠 Focus Areas
- Enumeration methodology
- Exploitation basics
- Post-exploitation and pivoting
- Report writing

### ✅ Stage 6 Complete When:
- Full course completed
- Every technique practiced hands-on in the lab

---

## Stage 7 — First Certification (eJPT)

> Your first official hands-on certification. This one counts.

### 📚 Course + Exam
- [ ] **INE — Penetration Testing Student** path (Free tier available)
  - Study the full course before attempting the exam
- [ ] **Sit the eJPT exam** — [ine.com/certifications/ejpt-certification](https://ine.com/certifications/ejpt-certification)

### 📝 Post-Exam
- [ ] Write a **professional report** documenting:
  - Your preparation process
  - Exam experience and approach
  - What you'd do differently
- [ ] Publish to GitHub under `/Certifications/eJPT/`

### ✅ Stage 7 Complete When:
- eJPT exam passed
- Professional preparation/exam report published to GitHub

---

## Stage 8 — Active Directory + OSCP Prep

> The final bridge before OSCP. Active Directory is everywhere in enterprise networks.

### 🧪 TryHackMe
- [ ] **"Attacktive Directory"** room
- [ ] **"Wreath"** network

### 🧠 Key Concepts to Master
- [ ] BloodHound — AD enumeration and attack path visualization
- [ ] Kerberoasting
- [ ] Pass-the-Hash
- [ ] Lateral movement techniques
- [ ] Privilege escalation in Windows environments

### 🖥️ HackTheBox
- [ ] **Starting Point machines** (Free tier)
  - Complete **15–20 easy retired machines**
  - This bridges the gap between TryHackMe and OSCP difficulty
  - **Rule:** Attempt every box yourself first — only watch IppSec walkthroughs after a genuine attempt

### ✅ Stage 8 Complete When:
- Both TryHackMe rooms completed
- 15–20 HTB machines rooted
- Comfortable with AD attack techniques

---

## Stage 9 — IoT Hacking Begins

### 📚 Course + Certification
- [ ] **TCM Security — Beginner's Guide to IoT and Hardware Hacking** (Udemy)
- [ ] **Sit the PIPA exam** (course includes exam voucher)

### 🛒 Hardware to Buy During This Stage
- [ ] **CH340 UART adapter** — serial communication with embedded devices
- [ ] **Cheap old router** from thrift store — make sure it supports **OpenWrt**
- [ ] **Logic analyzer clone** (e.g., 8-channel USB clone) — for signal analysis
- [ ] **Multimeter** — basic electronics, continuity testing, voltage checks

### 🔬 Practice
- [ ] Flash your thrift store router with OpenWrt
- [ ] Connect via UART and explore the boot process
- [ ] Capture traffic from the router using your Kali VM

### ✅ Stage 9 Complete When:
- TCM IoT course completed
- PIPA exam passed
- Hardware acquired and hands-on experiments started

---

## Stage 10 — Advanced IoT

> The most specialized stage. Build a portfolio that speaks for itself.

### 📚 Course + Certification
- [ ] **Virtual Hacking Labs — IoT Penetration Testing Essentials**
- [ ] **Sit the CIPT-01 exam** (~6 month study + exam plan)

### 📁 Portfolio Projects (Build 6–8 projects)

For each project:
- [ ] Conduct the full assessment
- [ ] Write a **professional pentest report**
- [ ] Publish to GitHub under `/Portfolio/Projects/`

**Project ideas:**
- Router firmware extraction and analysis
- UART shell access on embedded device
- Web interface assessment on IoT device
- Replay attack on wireless IoT sensor
- Firmware emulation with QEMU
- Bluetooth LE sniffing and analysis
- Custom Nmap scripts for IoT device fingerprinting
- Full assessment report on a home lab target device

### ✅ Stage 10 Complete When:
- CIPT-01 exam passed
- 6–8 portfolio projects completed with professional reports
- All work published to GitHub

---

## Stage 11 — Final Goal (OSCP)

> The certification that changes everything. Everything before this was preparation.

### 📚 Course + Exam
- [ ] **Offensive Security PEN-200** course
  - Work through every module
  - Complete all course exercises
  - Spend significant time in the PEN-200 lab environment
- [ ] **Sit the OSCP exam**

### 🧠 Exam Preparation Mindset
- You will have 24 hours to compromise machines
- Methodology and documentation matter as much as exploitation
- Rest the night before — seriously

### 📝 Post-OSCP
- [ ] Write a full retrospective report on your OSCP journey
- [ ] Update your GitHub, LinkedIn, and CV
- [ ] Plan the next phase

### ✅ Final Goal Complete When:
- OSCP earned ✅

---

## 📊 Progress Tracker

| Stage | Topic | Status |
|-------|-------|--------|
| 1 | Python + Linux Foundations | 🔄 In Progress |
| 2 | Networking | ⬜ Not Started |
| 3 | Security Fundamentals | ⬜ Not Started |
| 4 | Penetration Testing Basics | ⬜ Not Started |
| 5 | Web Application Security | ⬜ Not Started |
| 6 | Practical Pentesting | ⬜ Not Started |
| 7 | eJPT Certification | ⬜ Not Started |
| 8 | Active Directory + OSCP Prep | ⬜ Not Started |
| 9 | IoT Hacking Begins | ⬜ Not Started |
| 10 | Advanced IoT + CIPT-01 | ⬜ Not Started |
| 11 | OSCP | ⬜ Not Started |

---

## 🗂️ Repository Structure

```
Cyber-Learning/
├── Roadmap.md
├── Stage1/
│   └── Python-Learning/
├── Reports/
│   ├── Stage4/          ← TryHackMe Jr Pentester lab reports
│   └── Stage6/          ← Practical Ethical Hacking notes
├── Portfolio/
│   └── Projects/        ← IoT portfolio reports (Stage 10)
└── Certifications/
    ├── eJPT/            ← eJPT prep + exam report
    └── OSCP/            ← OSCP retrospective
```

---

## 🧭 Core Principles

1. **Do the work** — watching is not learning. Replicate everything hands-on.
2. **Document everything** — write reports, push to GitHub, build evidence of your skills.
3. **Run stages in parallel where noted** — Python + Bandit, Dion + Messer.
4. **Don't skip ahead** — each stage genuinely prepares you for the next.
5. **Consistency beats intensity** — showing up every day matters more than marathon sessions.

---

*Maintained by [uZiDuZi608](https://github.com/uZiDuZi608) & [Uzi14](https://github.com/Uzi14)*
