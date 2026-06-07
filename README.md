# <!-- Header Banner -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0F0C29,50:302B63,100:24243e&height=200&section=header&text=Renold%20Stephen&fontSize=48&fontColor=ffffff&fontAlignY=38&desc=AI%20Systems%20%7C%20Data%20Engineering%20%7C%20MLOps&descAlignY=58&descSize=20" />
</p>

<!-- Status Pills -->
<p align="center">
  <img src="https://img.shields.io/badge/🟢 Open To-AI%2FML%20%7C%20Data%20Engineering%20%7C%20MLOps-%230A66C2?style=flat-square" />
  &nbsp;
  <img src="https://img.shields.io/badge/M.Tech-Computer%20Science%20%7C%20Christ%20University-6C5B7B?style=flat-square" />
  &nbsp;
  <img src="https://img.shields.io/badge/📍-Bangalore%2C%20India-2C5364?style=flat-square" />
  &nbsp;
  <img src="https://komarev.com/ghpvc/?username=RenoX23&color=6C5B7B&style=flat-square&label=Profile+Views" />
</p>

---

## 👋 About

I build AI systems and data pipelines that work on real infrastructure.

My focus sits at the intersection of **agent-based AI**, **data engineering**, and **cloud-native MLOps** — I can wire a LangGraph multi-agent pipeline one day and tune an Isolation Forest on live Prometheus metrics the next.

- 🧠 **Current builds:** Multi-agent BI systems, Kubernetes ops intelligence, ML-based data quality monitoring
- 📊 **Data stack:** PostgreSQL · Airflow · dbt · Power BI · Streamlit · Plotly
- ☁️ **Infra stack:** Kubernetes · Prometheus · Docker · Terraform · Helm
- 🤖 **AI stack:** LangGraph · LangChain · Groq · RAG · Isolation Forest · scikit-learn
- 📝 **Published:** YOLOv5 + Raspberry Pi assistive system — IJIRT 2025
- 🎓 **Microsoft Learn Student Ambassador**

> 🔭 Dissertation: ML-Based Data Quality Monitoring Framework for Cloud-Native ETL Pipelines

---

## 🚀 Featured Projects

### 🧠 InternIQ — Multi-Agent Internship Market Analyst
> Autonomous 4-agent LangGraph pipeline answering natural language business questions over a proprietary internship dataset

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Streamlit-FF4B4B?style=flat-square&logo=streamlit)](https://interniq-multiagent-analyst-renox23.streamlit.app/)
[![Repo](https://img.shields.io/badge/GitHub-interniq--multiagent--analyst-181717?style=flat-square&logo=github)](https://github.com/RenoX23/interniq-multiagent-analyst)

- Built **LangGraph StateGraph** with 4 typed agent nodes: Planner → SQL Agent → Viz Agent → Insight Agent
- SQL Agent uses **few-shot prompting** over proprietary schema — 270 scraped Internshala listings, 1,339 skill records
- Auto-selects chart type (bar/pie/line) based on query semantics; generates 2-3 sentence analyst insight per query
- Deployed on **Streamlit Cloud** with **Neon serverless PostgreSQL** as backend

`LangGraph` `LangChain` `Groq LLaMA 3.3` `PostgreSQL` `Streamlit` `Plotly` `Neon`

---

### ⚙️ KubeIQ — Kubernetes Ops Intelligence Agent
> ML-driven SRE assistant — detects anomalous pods, retrieves runbooks, generates root cause analysis

[![Repo](https://img.shields.io/badge/GitHub-kubeiq--ops--agent-181717?style=flat-square&logo=github)](https://github.com/RenoX23/kubeiq-ops-agent)

- **Isolation Forest** on live Prometheus time-series (CPU, memory, restarts) — flags statistical outliers across all pods
- **TF-IDF RAG** retrieves relevant SRE runbooks per anomaly; no heavy embedding models required
- **LLM reasoning layer** produces structured Root Cause → Evidence → Remediation per flagged pod
- Stress-tested with real fault injection: cpu-stress pod flagged at 1.34 cores → LLM diagnosed "runaway process"

`Isolation Forest` `Prometheus` `Kind` `TF-IDF RAG` `Groq LLaMA 3.3` `Helm` `Streamlit`

---

### 📊 India Tech Internship Market Intelligence
> End-to-end scraping → PostgreSQL → SQL analytics → Power BI dashboard

[![Repo](https://img.shields.io/badge/GitHub-job--market--intelligence-181717?style=flat-square&logo=github)](https://github.com/RenoX23/job-market-intelligence)

- Scraped **757 Internshala listings** via BeautifulSoup; cleaned to 270 relevant records with 1,339 skill tags
- SQL analysis with **CTEs and window functions** — stipend benchmarking, skill demand ranking, location heatmaps
- 4-page **Power BI dashboard** — key finding: ML roles pay 2.4x more than DA roles (₹15.9K vs ₹6.5K/month)

`Python` `BeautifulSoup` `PostgreSQL` `SQL` `Power BI` `Pandas`

---

### 📈 DORA Metrics Engineering Dashboard
> GitHub API → SQLite → Streamlit — real DORA metrics across 5 open-source engineering orgs

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Streamlit-FF4B4B?style=flat-square&logo=streamlit)](https://renox23-dora-metrics-dashboard.streamlit.app/)
[![Repo](https://img.shields.io/badge/GitHub-dora--metrics--dashboard-181717?style=flat-square&logo=github)](https://github.com/RenoX23/dora-metrics-dashboard)

- Ingested 1,000 PRs, 250 releases, 1,000 issues via **PyGithub** across dbt-core, ArgoCD, Grafana, Airflow, Prometheus
- Computed weighted health scores: dbt-core 81.2 · ArgoCD 75.0 · Grafana 75.0
- Deployed on Streamlit Cloud with automated data refresh

`Python` `PyGithub` `SQLite` `Streamlit` `Plotly` `DORA Metrics`

---

### 🏠 Bangalore Rental Market Intelligence
> 886-listing dataset → zone-mapped analytics → Streamlit dashboard

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Streamlit-FF4B4B?style=flat-square&logo=streamlit)](https://renox23-bangalore-rental-dashboard.streamlit.app/)
[![Repo](https://img.shields.io/badge/GitHub-bangalore--rental--dashboard-181717?style=flat-square&logo=github)](https://github.com/RenoX23/bangalore-rental-dashboard)

- Mapped 127 localities to 6 Bangalore zones; engineered price-per-sqft metric across segments
- Key finding: Ramamurthy Nagar/K R Puram best value at ₹13-14/sqft vs Whitefield ₹31/sqft

`Python` `Pandas` `PostgreSQL` `Streamlit` `Plotly`

---

### 🔁 GitOps Infrastructure Automation & Observability Platform
> Production-grade GitOps pipeline with ArgoCD, Prometheus, Grafana, Terraform

[![Repo](https://img.shields.io/badge/GitHub-gitops--monitoring--project-181717?style=flat-square&logo=github)](https://github.com/RenoX23/gitops-monitoring-project)

- Automated Kubernetes cluster sync via **ArgoCD** — Git as single source of truth
- Custom **Prometheus** alert rules + **Grafana** dashboards for pod-level observability
- Infrastructure provisioned via **Terraform**; anomaly detection within 60 seconds of onset

`ArgoCD` `Kubernetes` `Prometheus` `Grafana` `Terraform` `Helm` `Flask`

---

## 🔧 Tech Stack

**AI & Agents**

![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square)
![LangGraph](https://img.shields.io/badge/LangGraph-302B63?style=flat-square)
![Groq](https://img.shields.io/badge/Groq-F55036?style=flat-square)
![RAG](https://img.shields.io/badge/RAG-TF--IDF%20%7C%20FAISS-4A90D9?style=flat-square)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-%23F7931E.svg?style=flat-square&logo=scikit-learn&logoColor=white)
![Python](https://img.shields.io/badge/Python-3670A0?style=flat-square&logo=python&logoColor=ffdd54)

**Data Engineering**

![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-%23150458.svg?style=flat-square&logo=pandas&logoColor=white)
![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=flat-square&logo=powerbi&logoColor=black)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=flat-square&logo=plotly&logoColor=white)

**Infrastructure & MLOps**

![Kubernetes](https://img.shields.io/badge/Kubernetes-%23326ce5.svg?style=flat-square&logo=kubernetes&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-%230db7ed.svg?style=flat-square&logo=docker&logoColor=white)
![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=flat-square&logo=prometheus&logoColor=white)
![Grafana](https://img.shields.io/badge/Grafana-%23F46800.svg?style=flat-square&logo=grafana&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-%235835CC.svg?style=flat-square&logo=terraform&logoColor=white)
![Helm](https://img.shields.io/badge/Helm-0F1689?style=flat-square&logo=helm&logoColor=white)
![ArgoCD](https://img.shields.io/badge/ArgoCD-%23EF7B4D.svg?style=flat-square&logo=argo&logoColor=white)

---

## 🎓 Background

| Degree | Institution | Focus |
|--------|-------------|-------|
| M.Tech — Computer Science | Christ University, Bangalore | AI Systems · Data Engineering · Cloud-Native MLOps |
| B.Tech — Information Science | Cambridge Institute of Technology | Full-Stack · DevOps |

📝 **Published:** YOLOv5 + Raspberry Pi Assistive Navigation System — IJIRT 2025  
🎓 **Microsoft Learn Student Ambassador**  
📍 Bangalore · Available immediately · On-site / Hybrid / Remote

---

## 📫 Connect

<p>
  <a href="https://www.linkedin.com/in/renoldstephen/">
    <img src="https://img.shields.io/badge/LinkedIn-Renold%20Stephen-%230A66C2?style=flat-square&logo=linkedin&logoColor=white" />
  </a>
  &nbsp;
  <a href="mailto:renoldstephen23@gmail.com">
    <img src="https://img.shields.io/badge/Email-renoldstephen23%40gmail.com-%23EA4335?style=flat-square&logo=gmail&logoColor=white" />
  </a>
  &nbsp;
  <a href="https://renold-cloudfolio.netlify.app/">
    <img src="https://img.shields.io/badge/Portfolio-renoldstephen-%23000000?style=flat-square&logo=netlify&logoColor=white" />
  </a>
</p>

<!-- Footer Banner -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:24243e,50:302B63,100:0F0C29&height=100&section=footer" />
</p>
