<div align="center">

<img src="./assets/hero-name.gif" alt="Renold Stephen R — AI Systems, Data Engineering, MLOps" width="100%" />

<img src="./assets/status-pills.svg" alt="AI Agents, ML Systems, Data Analytics, MLOps, Data Engineering" width="100%" />

</div>

<div align="center">

<a href="https://github.com/RenoX23"><img src="https://img.shields.io/badge/GitHub-RenoX23-0b0f14?style=for-the-badge&logo=github&logoColor=white&labelColor=111923" /></a>
<a href="https://www.linkedin.com/in/renoldstephen/"><img src="https://img.shields.io/badge/LinkedIn-Renold%20Stephen-0b0f14?style=for-the-badge&logo=linkedin&logoColor=0A66C2&labelColor=111923" /></a>
<a href="mailto:renoldstephen23@gmail.com"><img src="https://img.shields.io/badge/Email-Contact-0b0f14?style=for-the-badge&logo=gmail&logoColor=EA4335&labelColor=111923" /></a>

</div>

---

## `~/about`

<div align="center">

<img src="./assets/about-terminal.gif" alt="Terminal-style about section" width="100%" />

</div>

---
## `~/workflow`

<div align="center">

<img src="./assets/motion-flow.gif" alt="Animated AI engineering workflow" width="100%" />

</div>

**The pattern:** turn ambiguous problems into observable systems.

`INPUT` → `REASON` → `EXECUTE` → `OBSERVE`

---

## `~/stack`

<div align="center">

# 🛠️ Tech Stack & Arsenal

</div>

<details open>
<summary><b>🌐 Languages & Core Tech</b></summary>

<br/>

<div align="center">

<a href="#"><img src="https://skillicons.dev/icons?i=python,javascript,typescript,html,cpp,cs,java,go&theme=dark" alt="Languages and core technologies" /></a>

</div>

</details>

<br/>

<details open>
<summary><b>💻 Frameworks & Libraries</b></summary>

<br/>

<div align="center">

<a href="#"><img src="https://skillicons.dev/icons?i=react,nextjs,nodejs,tailwind,flask,fastapi,vite&theme=dark" alt="Frameworks and libraries" /></a>

</div>

</details>

<br/>

<details open>
<summary><b>🗄️ Database & Cloud</b></summary>

<br/>

<div align="center">

<a href="#"><img src="https://skillicons.dev/icons?i=postgres,mongodb,mysql,supabase,firebase,aws,gcp,vercel&theme=dark" alt="Database and cloud technologies" /></a>

</div>

</details>

<br/>


<details open>
<summary><b>🤖 AI & Data Science</b></summary>

<br/>

<div align="center">

<img src="https://skillicons.dev/icons?i=tensorflow,pytorch,opencv&theme=dark"
     alt="TensorFlow, PyTorch and OpenCV"
     height="72" />

<br/><br/>

<img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white"
     alt="NumPy" />
<img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white"
     alt="Pandas" />
<img src="https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white"
     alt="Scikit-learn" />
<img src="https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge"
     alt="LangChain" />
<img src="https://img.shields.io/badge/LangGraph-302B63?style=for-the-badge"
     alt="LangGraph" />
<img src="https://img.shields.io/badge/RAG-4A90D9?style=for-the-badge"
     alt="RAG" />

</div>

</details>


<details open>
<summary><b>⚙️ Infrastructure & MLOps</b></summary>

<br/>

<div align="center">

<a href="#"><img src="https://skillicons.dev/icons?i=docker,kubernetes,terraform,githubactions,jenkins,linux&theme=dark" alt="Infrastructure and MLOps technologies" /></a>

<br/><br/>

<img src="https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=prometheus&logoColor=white" alt="Prometheus" />
<img src="https://img.shields.io/badge/Grafana-F46800?style=for-the-badge&logo=grafana&logoColor=white" alt="Grafana" />
<img src="https://img.shields.io/badge/ArgoCD-EF7B4D?style=for-the-badge&logo=argo&logoColor=white" alt="ArgoCD" />
<img src="https://img.shields.io/badge/Helm-0F1689?style=for-the-badge&logo=helm&logoColor=white" alt="Helm" />

</div>

</details>

---

## `~/github-stats`

<div align="center">

<img src="./assets/stats-terminal.gif" alt="GitHub statistics" width="100%" />

</div>



## `~/projects`

<div align="center">

<img src="./assets/projects-terminal.gif" alt="Featured project terminal" width="100%" />

</div>

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
## `~/education`

<div align="center">

<img src="./assets/education-terminal.gif" alt="Terminal-style education and background" width="100%" />

</div>

## 🎓 Background

| Degree | Institution | Focus |
|--------|-------------|-------|
| M.Tech — Computer Science | Christ University, Bangalore | AI Systems · Data Engineering · Cloud-Native MLOps |
| B.Tech — Information Science | Cambridge Institute of Technology | Full-Stack · DevOps |

📝 **Published:** YOLOv5 + Raspberry Pi Assistive Navigation System — IJIRT 2025  
🎓 **Microsoft Learn Student Ambassador**  
📍 Bangalore · Available immediately · On-site / Hybrid / Remote

---




## `~/activity`



<br/>

<a href="https://github.com/RenoX23">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=RenoX23&bg_color=0b0f14&color=2de2c4&line=2de2c4&point=ffffff&area=true&hide_border=true&custom_title=LIVE%20GITHUB%20ACTIVITY" alt="Live GitHub activity graph" width="100%" />
</a>

</div>

<br/>

<div align="center">

<a href="https://github.com/RenoX23">
<img src="https://img.shields.io/github/followers/RenoX23?style=flat-square&label=Followers&color=2de2c4&labelColor=111923" />
</a>
<a href="https://github.com/RenoX23?tab=stars">
<img src="https://img.shields.io/github/stars/RenoX23?affiliations=OWNER&style=flat-square&label=Stars&color=5aa9ff&labelColor=111923" />
</a>
<a href="https://komarev.com/ghpvc/?username=RenoX23">
<img src="https://komarev.com/ghpvc/?username=RenoX23&style=flat-square&color=a78bfa&label=Profile%20Views" />
</a>

</div>

---

## `~/connect`

<div align="center">

<img src="./assets/connect-terminal.gif" alt="Contact links terminal" width="100%" />

<br/><br/>

[![GitHub](https://img.shields.io/badge/GitHub-RenoX23-0b0f14?style=for-the-badge&logo=github&logoColor=white&labelColor=111923)](https://github.com/RenoX23)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Renold%20Stephen-0b0f14?style=for-the-badge&logo=linkedin&logoColor=0A66C2&labelColor=111923)](https://www.linkedin.com/in/renoldstephen/)
[![Email](https://img.shields.io/badge/Email-renoldstephen23-0b0f14?style=for-the-badge&logo=gmail&logoColor=EA4335&labelColor=111923)](mailto:renoldstephen23@gmail.com)
[![Portfolio](https://img.shields.io/badge/Portfolio-renold--cloudfolio-0b0f14?style=for-the-badge&logo=netlify&logoColor=00C7B7&labelColor=111923)](https://renold-cloudfolio.netlify.app/)

### `> let's build something useful together.`

</div>

---

<div align="center">

`RenoX23` · AI Systems · Data Engineering · MLOps

</div>
