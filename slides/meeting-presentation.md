---
marp: true
theme: default
paginate: true
header: AI-Powered Internal Developer Framework
footer: August 2026
style: |
  section {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: linear-gradient(135deg, #f0f4ff 0%, #e8f0ff 50%, #f5f0ff 100%);
    color: #1a202c;
    font-size: 26px;
    padding: 60px 70px;
  }
  section.lead {
    text-align: center;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
  }
  section.lead h1 {
    font-size: 2.8em;
    font-weight: bold;
    margin-bottom: 0.3em;
    color: #fff;
  }
  section.lead h2 {
    font-size: 1.4em;
    font-weight: normal;
    opacity: 0.95;
    color: #fff;
  }
  section.lead h3 {
    color: #fff !important;
    opacity: 0.9;
  }
  section.lead p, section.lead ul, section.lead ol {
    color: #fff !important;
  }
  section.lead header, section.lead footer {
    color: rgba(255,255,255,0.8) !important;
  }
  section.lead::after {
    color: rgba(255,255,255,0.8) !important;
  }
  section.lead code {
    color: #fff !important;
    background: rgba(255,255,255,0.15) !important;
  }
  h1 {
    color: #5b21b6;
    border-bottom: 3px solid #7c3aed;
    padding-bottom: 0.2em;
    margin-bottom: 0.4em;
    font-size: 1.5em;
    font-weight: 700;
  }
  h2 {
    color: #7c3aed;
    font-size: 1.2em;
    margin-bottom: 0.3em;
    font-weight: 600;
  }
  h3 {
    font-size: 1em;
    margin-bottom: 0.2em;
    color: #6d28d9;
  }
  p, ul, ol {
    margin-bottom: 0.3em;
    line-height: 1.35;
    color: #2d3748;
  }
  li {
    margin-bottom: 0.1em;
    color: #2d3748;
  }
  code {
    background: rgba(124, 58, 237, 0.1);
    color: #5b21b6;
    padding: 0.1em 0.3em;
    border-radius: 3px;
    font-size: 0.85em;
  }
  pre {
    background: #f7f7fb;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    padding: 0.6em;
    font-size: 0.75em;
    line-height: 1.3;
    margin-bottom: 0.3em;
    color: #1a202c;
  }
  pre code {
    padding: 0;
    color: #1a202c;
  }
  table {
    width: 100%;
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    font-size: 0.85em;
    border-collapse: separate;
    border-spacing: 0;
    box-shadow: 0 1px 3px rgba(0,0,0,0.08);
  }
  th {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
    color: #ffffff !important;
    padding: 0.5em 0.7em;
    font-weight: 600;
    text-align: left;
    border: none;
  }
  td {
    color: #2d3748 !important;
    background: #ffffff !important;
    padding: 0.4em 0.7em;
    border-top: 1px solid #e2e8f0;
    border-bottom: 1px solid #e2e8f0;
  }
  tr:nth-child(even) td {
    background: #f8f9ff !important;
  }
  .columns {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0.8em;
  }
  .highlight {
    background: rgba(124, 58, 237, 0.08);
    padding: 0.4em 0.6em;
    border-radius: 5px;
    border-left: 4px solid #7c3aed;
    color: #2d3748;
  }
  .compact ul {
    margin: 0;
    padding-left: 1.2em;
  }
  .compact li {
    margin-bottom: 0;
    line-height: 1.3;
  }
  header, footer {
    color: #64748b !important;
    font-size: 14px;
  }
  header::after, footer::after {
    color: #64748b !important;
  }
  section::after {
    color: #64748b !important;
  }
---

<!-- _class: lead -->

# จากไอเดียสู่ระบบจริง

## ง่ายกว่าที่คิด

<p style="color: white; opacity: 0.9; font-size: 1.2em; margin-top: 0.5em;">AI-Powered Internal Developer Framework</p>

<p style="color: white; opacity: 0.85; font-size: 1em; margin-top: 1em;">สนับสนุนทุกไอเดีย ให้ deploy ได้เร็ว ปลอดภัย และยั่งยืน</p>

<p style="color: white; opacity: 0.8; font-size: 0.9em; margin-top: 2em;">สิงหาคม 2026</p>

---

# 🎯 วาระการประชุม (90 นาที)

| ขั้นตอน | หัวข้อ | เวลา |
|---------|--------|-------|
| 1 | 🌟 จุดเริ่มต้น: ไอเดียที่ดีสมควรได้รับการสนับสนุน | 15 นาที |
| 2 | 🚀 Journey: จากไอเดียสู่ระบบจริง | 20 นาที |
| 3 | 🤝 ทีมของเรา: ใครช่วยอะไรได้บ้าง | 15 นาที |
| 4 | 📚 AI ช่วยอะไรได้บ้าง | 15 นาที |
| 5 | 💡 เริ่มต้นอย่างไร | 15 นาที |

---

# 👥 องค์ประชุม (1/2)

<div class="columns">
<div>

**Maintenance (User)**
- แชร์ไอเดียและความต้องการ
- ให้ feedback
- เลือก pilot projects

**SA**
- ออกแบบ architecture
- Wiki schema
- Approval workflow

</div>
<div>

**AI-Eng**
- LLM integration
- Auto-doc generation
- MCP, auto PR

**Dev**
- Implementation
- Workflow, templates

</div>
</div>

---

# 👥 องค์ประชุม (2/2)

**Infra&Security**
- k3s, GitLab, ArgoCD
- Vault, RBAC, monitoring
- Network policies

---

<!-- _class: lead -->

# 🌟 ขั้นตอนแรก

## จุดเริ่มต้น: ไอเดียที่ดีสมควรได้รับการสนับสนุน

**เวลา: 15 นาที | ผู้นำเสนอ: Maintenance (User)**

---

# 💭 อะไรที่ทำให้คนอยาก deploy เร็ว?

<div class="highlight">

**จากประสบการณ์ที่ผ่านมา:**
- 🌱 คนที่มีไอเดียดี มักอยากเห็นผลงานตัวเองทำงานเร็ว
- 🌱 กระบวนการปัจจุบันอาจยังไม่ทันกับความรวดเร็วของไอเดีย
- 🌱 เครื่องมือที่มีอยู่อาจยังไม่ตอบโจทย์ self-service

</div>

**คำถามเปิด:** มีประสบการณ์อะไรที่อยากแชร์บ้างคะ?

---

# 💡 สิ่งที่เรามาเรียนรู้ร่วมกัน

<div class="columns">
<div class="compact">

**ความท้าทายด้านกระบวนการ**
- รอ approval นาน
- Infra อาจยังไม่พร้อมทันที

**ความท้าทายด้านเครื่องมือ**
- ไม่มี self-service
- ต้องพึ่ง infra team

</div>
<div class="compact">

**ความท้าทายด้านข้อมูล**
- ขาด documentation ที่ทันสมัย
- ความรู้กระจายอยู่ตามตัวบุคคล

**โอกาสในการพัฒนา**
- ทำให้ทุกขั้นตอนง่ายและเร็วขึ้น
- สนับสนุนคนที่มีไอเดียดี

</div>
</div>

---

# 🎯 สิ่งที่เราอยากสนับสนุน

<div class="highlight">

**สิ่งที่ควรมี:**
- ✅ ใช้ง่ายเหมือน Vercel/Render
- ✅ Self-service deployment
- ✅ LLM integration + Auto-documentation
- ✅ AI-assisted development

**คำถามเปิด:** ต้องการอะไรเพิ่มเติม? มีข้อจำกัดอะไร?

</div>

---

# 📊 Output ของขั้นตอนแรก

**รายการสิ่งที่เราอยากสนับสนุน (จัดลำดับความสำคัญ):**

1. _________________________
2. _________________________
3. _________________________
4. _________________________
5. _________________________

---

<!-- _class: lead -->

# 🚀 ขั้นตอนที่สอง

## Journey: จากไอเดียสู่ระบบจริง

**เวลา: 20 นาที | ผู้นำเสนอ: SA**

---

# 🏗️ Architecture Overview

```
💡 ไอเดีย → 💻 Code → 🤖 Auto Test → 📚 AI Docs → ✅ Review → 🚀 Deploy
                ↓           ↓              ↓          ↓          ↓
              GitLab    GitLab CI/CD     LLM Wiki   SA/SME    ArgoCD
              Push        (Pipeline)    (Qwen AI)   Review    → k3s
```

---

# 🎁 สิ่งที่ Framework จะมอบให้ (1/2)

<div class="columns">
<div class="compact">

**1. Self-Service Deployment**
- ใช้ง่ายเหมือน Vercel
- Deploy บน k3s ขององค์กร

**2. AI-Powered Documentation**
- LLM สร้าง wiki อัตโนมัติ
- อัพเดทเมื่อ code เปลี่ยน

</div>
<div class="compact">

**3. Knowledge Management**
- ระบบ approve ก่อน publish
- Version control

**4. Auto Code Review**
- AI ตรวจ code quality, security

</div>
</div>

---

# 🎁 สิ่งที่ Framework จะมอบให้ (2/2)

<div class="columns">
<div class="compact">

**5. MCP Integration**
- ทุก app มี MCP server
- AI agent ใช้งานได้ทันที

</div>
<div class="compact">

**6. Governance & Support**
- สนับสนุนเต็มที่
- ตรวจสอบได้
- Audit trail

</div>
</div>

---

# 🛠️ Tech Stack (1/2)

| Layer | Tool | หน้าที่ |
|-------|------|---------|
| Git + CI | **GitLab** | Git server + CI/CD pipeline |
| CD | **ArgoCD** | GitOps deploy to k3s |
| Orchestration | **k3s** | Lightweight Kubernetes |

---

# 🛠️ Tech Stack (2/2)

| Layer | Tool | หน้าที่ |
|-------|------|---------|
| LLM Gateway | **LiteLLM** | Cache, log, route LLM calls |
| LLM | **Alibaba Qwen** | Token Plan (credit-based) |
| Secrets | **Vault** | API keys, credentials |
| Registry | **Harbor** | Container images |
| Monitoring | **Prometheus + Grafana** | Metrics, dashboards |

---

<!-- _class: lead -->

# 🤝 ขั้นตอนสาม

## ทีมของเรา: ใครช่วยอะไรได้บ้าง

**เวลา: 15 นาที | ผู้นำเสนอ: ทุกทีม**

---

# 👥 ทีมพร้อมสนับสนุน

| ทีม | หน้าที่ | ช่วยอะไรได้บ้าง |
|------|--------|-----------------|
| **SA** | Architecture | ออกแบบระบบ, wiki schema |
| **AI-Eng** | LLM Integration | Auto-docs, MCP, AI review |
| **Dev** | Implementation | Workflow, templates |
| **Infra** | Infrastructure | k3s, monitoring, security |

**คุณแค่มีไอเดีย — ที่เหลือเราช่วย!**

---

# 📚 LLM Wiki คืออะไร?

<div class="highlight">

**หลักการ: ทุก app มี documentation อัตโนมัติ**

- AI อ่าน code + design docs → สร้าง structured wiki อัตโนมัติ
- เก็บเป็น markdown files (ไม่ต้องใช้ vector DB)
- อัพเดทอัตโนมัติเมื่อ code เปลี่ยน

</div>

---

# 🔄 Workflow

```
1. Dev push code → GitLab CI/CD pipeline trigger
                    ↓
2. LLM (Qwen) อ่าน code → สร้าง wiki pages
                    ↓
3. Wiki ถูก commit กลับเข้า repo
                    ↓
4. SA/SME review → approve/reject
                    ↓
5. approve → อนุญาต deploy | reject → แจ้ง Dev แก้ไข
```

---

# 📂 โครงสร้าง LLM Wiki

```
project-wiki/
├── raw/              ← source material (code, design docs)
├── wiki/             ← AI-generated structured knowledge
│   ├── index.md
│   ├── architecture.md
│   ├── api-reference.md
│   ├── deployment-guide.md
│   └── troubleshooting.md
└── outputs/          ← reports, answers
```

---

# ✅ KM Approval Process

<div class="columns">
<div class="compact">

**SME Review**
- Subject Matter Expert review ทุก wiki page

**Version Control**
- Track การเปลี่ยนแปลง, Rollback ได้

</div>
<div class="compact">

**Periodic Review**
- ตั้งเวลา review ทุก 6 เดือน

**Audit Log**
- รู้ว่าใคร approve, เมื่อไหร่, อะไรเปลี่ยน

</div>
</div>

---

# 🤔 ทำไมต้อง Approve?

<div class="highlight">

**เพื่อสร้างคุณภาพ:**
- ✅ ข้อมูลถูกต้อง เป็นปัจจุบัน
- ✅ Documentation ที่เชื่อถือได้
- ✅ Quality assurance + Accountability

**เพื่อสร้างความเป็นเจ้าของ:**
- ✅ ทีมช่วยกันตรวจสอบ
- ✅ ทุกคนมีส่วนร่วมในการสร้างความรู้

</div>

---

<!-- _class: lead -->

# 📚 ขั้นตอนสี่

## AI ช่วยอะไรได้บ้าง

**เวลา: 15 นาที | ผู้นำเสนอ: AI-Eng**

---

# 🎯 LiteLLM คืออะไร?

<div class="columns">
<div class="compact">

**LLM Gateway**
- รวม LLM calls ทั้งหมดที่เดียว

**Caching**
- Cache input/output → ลด cost, เพิ่ม speed

</div>
<div class="compact">

**Logging**
- Log ทุก call → ทำเป็น knowledge base

**Rate Limiting**
- ควบคุม usage per project

</div>
</div>

---

# 💰 Alibaba Token Plan

**คิดแบบ Credit ไม่ใช่ per-call**

| Seat Type | Price | Quota |
|-----------|-------|-------|
| Standard | $30/seat/mo | 25,000 credits |
| Pro | $100/seat/mo | 100,000 credits |
| Max | $200/seat/mo | 250,000 credits |

**Models:** Qwen, DeepSeek, Kimi, GLM, MiniMax

---

# 💰 Alibaba Token Plan — Models

| Brand | Models |
|-------|--------|
| Qwen | qwen3.7-max, qwen3.7-plus, qwen3.6-plus, qwen3.6-flash |
| DeepSeek | deepseek-v4-pro, deepseek-v4-flash, deepseek-v3.2 |
| Kimi | kimi-k2.7-code, kimi-k2.6, kimi-k2.5 |
| GLM | glm-5.2, glm-5.1, glm-5 |
| MiniMax | MiniMax-M2.5 |

---

# 🏗️ Architecture

```
User Request → 9router (round-robin)
                    ↓
              LiteLLM Proxy
                    ↓
         ┌─────────┴─────────┐
    API Key 1            API Key 2
    (Seat 1)             (Seat 2)
         └─────────┬─────────┘
              Alibaba Qwen API
```

**ประโยชน์:** กระจาย load, หลีกเลี่ยง rate limits, serve 10+ users

---

# 🧠 Knowledge Base จาก LLM Logs

<div class="highlight">

**Input/Output ที่ log ไว้ใน LiteLLM:**
- นำมาสร้าง wiki ได้
- Cache hits → ลด cost, เพิ่ม speed

**Workflow:**
```
LLM Call → LiteLLM Log → Langfuse → Analyze → Wiki Update
```

</div>

---

<!-- _class: lead -->

# 💡 ขั้นตอนห้า

## เริ่มต้นอย่างไร

**เวลา: 15 นาที | ผู้นำเสนอ: ทุกทีม**

---

# 🌟 3 ขั้นตอนง่ายๆ

<div class="columns">
<div>

**1. แชร์ไอเดีย**
- บอกเราว่าอยากทำอะไร
- ไม่ต้องมี code ก็ได้

</div>
<div>

**2. ทีมช่วย setup**
- เราเตรียม infra ให้
- AI ช่วยสร้างเอกสาร

</div>
</div>

<div class="highlight">

**3. Deploy ได้เลย**
- ใช้ง่ายเหมือน Vercel
- แต่ปลอดภัย + มี backup + มี monitoring

</div>

---

# 🔌 Network & Access: ไม่ต้องกังวลเรื่อง Port และ DNS

<div class="highlight">

**ปัญหาเดิม:**
- ❌ User ต้องรู้ว่า app รันบน port ไหน
- ❌ ต้องเปิด ticket ขอ IT สร้าง DNS record (รอ 1-3 วัน)
- ❌ IT เป็น bottleneck สร้าง DNS ให้ทุก app

**วิธีแก้:**
- ✅ **Wildcard DNS** — IT ทำครั้งเดียว `*.apps.company.com`
- ✅ **Ingress Controller** — Traefik จัดการ routing อัตโนมัติ
- ✅ **ไม่ต้องเปิด ticket อีกเลย!**

</div>

---

# 🌐 Wildcard DNS: IT ทำครั้งเดียว จบ!

<div class="columns">
<div>

**สิ่งที่ IT ทำ (ครั้งเดียว):**
1. สร้าง DNS: `*.apps.company.com`
2. ชี้ไป IP ของ k3s cluster
3. ตั้งค่า TLS certificate (Let's Encrypt)

**เสร็จแล้ว!** ไม่ต้องทำอะไรอีก

</div>
<div>

**สิ่งที่ User ทำ:**
```yaml
# แค่กำหนดชื่อใน Ingress
spec:
  rules:
  - host: my-app.apps.company.com
```

**ผลลัพธ์:**
- ✅ App เข้าถึงได้ทันที
- ✅ ไม่ต้องรอ IT
- ✅ ไม่ต้องรู้ port

</div>
</div>

---

# 🚀 ตัวอย่าง: Deploy แล้วได้ URL ทันที

```bash
# User push code → GitLab CI/CD deploy
$ git push origin main

# GitLab CI/CD สร้าง Ingress อัตโนมัติ
$ kubectl apply -f ingress.yaml

# ✅ App พร้อมใช้งาน!
🎉 Your app is live at: http://my-app.apps.company.com
```

**ไม่ต้อง:**
- ❌ เปิด ticket ขอ DNS
- ❌ รอ IT สร้าง record
- ❌ รู้ว่า app รันบน port ไหน
- ❌ ตั้งค่า firewall

**แค่ push code → ได้ URL ทันที!**

---

# 📅 Phase 1: Foundation (Month 1-2)

<div class="compact">

**Infrastructure Setup:**
- [ ] Setup k3s cluster (3 nodes)
- [ ] Setup GitLab + GitLab Runner
- [ ] Deploy ArgoCD, Harbor, Traefik
- [ ] Deploy LiteLLM + Redis + Langfuse

**Deliverables:** k3s cluster + GitLab repo + LLM gateway

</div>

---

# 📅 Phase 2: Automation (Month 3-4)

<div class="compact">

**AI Integration:**
- [ ] Integrate Alibaba Qwen API
- [ ] Build auto-doc generation pipeline
- [ ] Implement KM approval workflow
- [ ] Create MCP server template

**Deliverables:** Auto-doc + KM workflow + MCP template

</div>

---

# 📅 Phase 3: Polish (Month 5-6)

<div class="compact">

**User Experience:**
- [ ] Build self-service portal
- [ ] Implement governance policies
- [ ] Onboard 3 pilot projects
- [ ] Training & documentation

**Deliverables:** Portal + 3 pilots + Training materials

</div>

---

# 🔌 MCP Server Auto-Registration

**ทุก app มี MCP server**

```python
from fastmcp import FastMCP
mcp = FastMCP("my-app")

@mcp.tool()
def query_data(query: str) -> dict:
    """Query data from app"""
    pass
```

Auto-register to MCP catalog on deploy

---

# 🤖 Auto MR & Code Review

```yaml
stages:
  - review

ai-review:
  stage: review
  image: python:3.11
  rules:
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event"'
  script:
    - pip install openai
    - python scripts/ai-review.py
      --llm_endpoint "http://litellm:4000/v1"
      --model "qwen-plus"
      --mr_iid $CI_MERGE_REQUEST_IID
```

---

# 🚀 Immediate Actions (สัปดาห์หน้า)

<div class="columns">
<div class="compact">

**Infra&Security:**
- Setup k3s cluster (test)
- Deploy LiteLLM + Redis

**AI-Eng:**
- ทดสอบ Alibaba Qwen API
- สร้าง prototype auto-doc

</div>
<div class="compact">

**SA:**
- ออกแบบ wiki schema
- กำหนด KM approval criteria

**Dev:**
- Setup GitLab CI/CD pipelines
- สร้าง project template

</div>
</div>

---

# 🎯 Pilot Projects

**เลือก 3 projects จาก Maintenance (User)**

**Criteria:**
- Complexity ปานกลาง
- Team พร้อมร่วมมือ
- มี business impact ชัดเจน

**Timeline:** Onboard 2 สัปดาห์ → Deploy แรกภายใน 1 เดือน

---

# 📊 Success Metrics

<div class="columns">
<div class="compact">

**Developer Satisfaction**
- Target: >80% satisfaction

**Deployment Time**
- Target: <15 นาที

</div>
<div class="compact">

**Documentation Coverage**
- Target: 100% มี wiki

**Self-driven Solutions on Internal Platform**
- Target: เพิ่ม 50% ใน 3 เดือน

</div>
</div>

---

# 📝 Summary

<div class="columns">
<div class="compact">

**จุดเริ่มต้น:**
- ไอเดียที่ดีสมควรได้รับการสนับสนุน
- ทำให้ทุกขั้นตอนง่ายและเร็วขึ้น

**แนวทาง:**
- AI-Powered Framework
- LLM Wiki + KM Approval

</div>
<div class="compact">

**Tech Stack:**
- k3s + ArgoCD + GitLab
- LiteLLM + Alibaba Qwen

**Timeline:** 6 months, 3 phases

</div>
</div>

---

<!-- _class: lead -->

# 🙏 ขอบคุณค่ะ

## ทุกไอเดียสมควรได้รับการสนับสนุน

**Project:** `~/projects/ai-powered-internal-developer-framework`

---

# 📎 Appendix: Backup Data

<div class="compact">

**ข้อมูลสำรอง (ไม่พูดในการประชุม):**

1. **Alibaba Token Plan Details**
   - Full model list, credit calculation, pricing
   - ดูที่: `docs/backup/alibaba-token-plan.md`

2. **CI/CD Comparison**
   - GitLab CI vs GitHub Actions vs Argo Workflows
   - ดูที่: `docs/backup/cicd-comparison.md`

</div>
