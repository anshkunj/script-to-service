<p align="center">
  <img src="https://github.com/anshkunj/script-to-service/blob/82d20afb44f83c4eccd9d4825e4938b7fada4b9c/file_00000000f57072088cce7b4735829fd1.png" alt="Script→ Service" width="1200">
</p>

<h1 align="center">Script→ Service</h1>
<p align="center">Turning everyday scripts into live, production-ready services 🚀</p>


# Script → Service
**Turning boring manual workflows into live automation services**

Most automation dies as scripts.  
This project demonstrates a **repeatable system** for converting one-off Python scripts into **deployable, reliable services** with APIs, scheduling, logs, and real outputs.

This is not a demo app.  
It is a **pattern**.

---

## Why this exists

### Before
- Manual CSV / data cleanup  
- Local scripts run by one person  
- No logs, no retries  
- Not shareable, not reliable  

### After
- Live API endpoints  
- Scheduled automation  
- Logs, retries, health checks  
- Deployed as a service  

**Same logic. Production form.**

---

## The Script → Service approach

Every automation follows the same lifecycle:

1. **Script**  
   Start with a focused Python script that solves a real task.

2. **Service**  
   Wrap it with an API, validation, logging, and error handling.

3. **Deploy**  
   Ship it as a live service with predictable behavior.

4. **Repeat**  
   Apply the same structure to different workflows.

This repository captures that pattern.

---

## What’s included

- Automation engine (Python)
- FastAPI service wrapper
- Structured logging
- Basic retry & failure handling
- Health endpoint
- Example workflows
- Render-ready deployment

No heavy UI.  
No overengineering.

---

## Example workflows

Each example uses the **same architecture** — only the logic changes.

- **CSV → Report Automation**  
  Upload CSV → process → generate output

- **API Sync Job**  
  Fetch external API → normalize → store results

- **Data Cleanup Pipeline**  
  Raw input → validation → clean output

The value is the **repeatable system**, not the individual script.

---

## Live demo

> Replace the URLs below with your actual deployed service.

- Base URL: `https://<your-render-service>.onrender.com`
- API docs: `/docs`
- Health check: `/health`
- Run example: `/run/csv-report`

Seeing it run matters more than reading code.

---

## Repository structure

```
script-to-service/
├── engine/
│   ├── runner.py        # core execution logic
│   ├── scheduler.py    # scheduled jobs
│   └── validator.py    # input validation
│
├── api/
│   ├── main.py         # FastAPI entrypoint
│   ├── routes.py
│   └── auth.py
│
├── examples/
│   ├── csv_to_report.py
│   ├── api_sync.py
│   └── cleanup_task.py
│
├── README.md
└── DEPLOY.md
```
>If you understand this structure, you understand the project.

---

## Production signals

This project intentionally includes:

- Explicit input validation
- Structured logs
- Predictable failure behavior
- Environment-based configuration
- Health checks

Small details — but these separate **scripts** from **services**.

---

## Who this is for

- Teams stuck with manual workflows
- Developers shipping scripts that should be services
- Anyone who wants automation they can **trust**

---

## Philosophy

> Automation is only valuable when it is reliable, deployable, and repeatable.

**Script → Service** is how I approach automation.

---

## 👤 Author
**anshkunj**  
>Built as part of my **Script → Service** work —  
turning boring manual work into live automation services.

### 📫 Let’s connect
- **GitHub:** https://github.com/anshkunj
- **LinkedIn:** https://linkedin.com/in/anshkunj
- **Portfolio:** https://anshkunj.github.io/Portfolio
- **LeetCode:** https://leetcode.com/u/anshkunj
- **Devpost:** https://devpost.com/anshkunj
- **HackerRank:** https://www.hackerrank.com/profile/anshkunj
- **AtCoder:** https://atcoder.jp/users/anshkunj
- **Codeforces:** https://codeforces.com/profile/anshkunj
- **Fiverr:** https://www.fiverr.com/anshkunj
- **Freelancer:** https://www.freelancer.com/u/anshkunj

---

## ⭐ Support
If you found this project helpful, give it a star ⭐  
It motivates me to build more real-world projects 🚀

---

## 🔹 Note
This repository is regularly updated with new scripts and improvements. 