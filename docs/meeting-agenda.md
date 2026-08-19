# วาระการประชุม: AI-Powered Internal Developer Framework
**เวลาทั้งหมด:** 90 นาที (1 ชั่วโมง 30 นาที)

---

## 🎯 วาระที่ 1: ปัญหาปัจจุบัน — ทำไม User ถึง Deploy แอพนอกองค์กร? (20 นาที)

**วัตถุประสงค์:** รับฟัง Pain Points จากผู้ใช้จริง เพื่อเข้าใจ root cause

**คำถามกระตุ้นการสนทนา:**

### 1. ทำไมถึงเลือก deploy นอกองค์กร?
- กระบวนการในองค์กรช้าเกินไป? (รอ approval นาน, infra ไม่พร้อม)
- เครื่องมือในองค์กรใช้งานยาก? (ไม่มี self-service, ต้องพึ่ง infra team)
- ไม่รู้ว่าองค์กรมีอะไรให้ใช้? (ขาด communication, documentation)

### 2. ปัญหาที่เจอจากการ deploy นอกองค์กร:
- **Security Risk:** ข้อมูลบริษัทอยู่บน Vercel/Render ที่องค์กรควบคุมไม่ได้
- **Compliance:** ไม่เป็นไปตาม PDPA, ISO, หรือ internal policy
- **Cost:** จ่ายเงินเองแล้วองค์กรไม่ reimburse? หรือองค์กรเสียโอกาสในการ negotiate enterprise deal?
- **Maintenance:** ไม่มี backup, monitoring, หรือ incident response จากองค์กร
- **Knowledge Loss:** ไม่มี documentation, ถ้าคนพัฒนาออกก็ไม่มีใคร maintain ต่อได้

### 3. สิ่งที่ต้องการจาก framework ภายใน:
- ใช้ง่ายเหมือน Vercel/Render ไหม?
- ต้องการอะไรเพิ่มเติม? (LLM integration, auto-documentation, AI-assisted development)

**ผู้รับผิดชอบ:** Maintenance (User) เป็นคนเล่า, คนอื่นรับฟังและจดบันทึก

**Output:** รายการ Pain Points ที่จัดลำดับความสำคัญแล้ว

---

## 💡 วาระที่ 2: แนวทางแก้ไข — สิ่งที่ควรจะเป็น (15 นาที)

**วัตถุประสงค์:** นำเสนอ vision ของ Internal Developer Framework ที่แก้ปัญหาทั้งหมด

**Concept:**
```
Developer → Gitea Push → Gitea Actions (CI) → Auto Doc Gen → KM Approval → ArgoCD (CD) → k3s → MCP Auto-Register
```

**สิ่งที่ framework ใหม่จะมอบให้:**
1. **Self-Service Deployment** — ใช้ง่ายเหมือน Vercel, แต่ deploy บน k3s ขององค์กร
2. **AI-Powered Documentation** — LLM สร้าง wiki อัตโนมัติจาก code
3. **Knowledge Management** — มีระบบ approve ก่อน publish
4. **Auto Code Review** — AI ตรวจ code quality, security
5. **MCP Integration** — ทุก app มี MCP server ให้ AI agent ใช้งานได้ทันที
6. **Governance & Compliance** — ควบคุมได้, ตรวจสอบได้, เป็นไปตาม policy

**Tech Stack Overview:**
- **k3s** (lightweight Kubernetes) + **ArgoCD** (GitOps)
- **Gitea** (Git) + **Gitea Actions** (CI/CD)
- **LiteLLM** (LLM Gateway) + **Alibaba Qwen** (Token Plan)
- **Vault** (Secrets) + **Prometheus/Grafana** (Monitoring)

**ผู้รับผิดชอบ:** SA นำเสนอ, AI-Eng เสริมเรื่อง LLM integration

---

## 📚 วาระที่ 3: LLM Wiki + Knowledge Management Approval (15 นาที)

**วัตถุประสงค์:** อธิบายว่า LLM Wiki ช่วยได้อย่างไร และมีระบบ approve อย่างไร

### LLM Wiki คืออะไร?
- AI อ่าน code + design docs แล้วสร้าง structured wiki อัตโนมัติ
- เก็บเป็น markdown files (ไม่ต้องใช้ vector DB)
- อัพเดทอัตโนมัติเมื่อ code เปลี่ยน

### Workflow:
```
1. Dev push code → Gitea Actions trigger
2. LLM (Qwen) อ่าน code → สร้าง wiki pages
3. Wiki ถูก commit กลับเข้า repo
4. SA/SME review → approve/reject
5. ถ้า approve → อนุญาต deploy
6. ถ้า reject → แจ้ง Dev แก้ไข
```

### KM Approval Process:
- **SME (Subject Matter Expert)** review ทุก wiki page
- **Version Control** — track การเปลี่ยนแปลง, rollback ได้
- **Periodic Review** — ตั้งเวลา review ทุก 6 เดือน
- **Audit Log** — รู้ว่าใคร approve, เมื่อไหร่, อะไรเปลี่ยน

### ทำไมต้อง approve?
- ป้องกันข้อมูลผิดๆ ถูก publish
- รับรองว่า documentation ถูกต้องและ up-to-date
- สร้าง trust ว่า wiki ใช้ได้จริง

**เครื่องมือ:**
- **Wiki Builder** (Claude Code plugin) หรือ custom script
- **Alibaba Qwen API** สำหรับ generate docs
- **Gitea Pull Request** สำหรับ review & approve

**ผู้รับผิดชอบ:** SA (schema, approval criteria), AI-Eng (LLM pipeline)

---

## 🔌 วาระที่ 4: LiteLLM + LLM Architecture (10 นาที)

**วัตถุประสงค์:** อธิบาย concept สั้นๆ (ไม่ลงรายละเอียด)

### LiteLLM คืออะไร?
- **LLM Gateway** — รวม LLM calls ทั้งหมดที่เดียว
- **Caching** — cache input/output ลด cost, เพิ่ม speed
- **Logging** — log ทุก call เพื่อ observability → ทำเป็น knowledge base
- **Rate Limiting** — ควบคุม usage per project

### Alibaba Token Plan:
- **คิดแบบ Credit** ไม่ใช่ per-call
- **Prepaid** — ซื้อ credit ล่วงหน้า, ใช้เท่าไหร่หักเท่านั้น
- **Multiple Models** — Qwen, DeepSeek, Kimi, GLM, MiniMax
- **Architecture:** 9router + LiteLLM round-robin

### Knowledge Base จาก LLM Logs:
- Input/output ที่ log ไว้ใน LiteLLM → นำมาสร้าง wiki ได้
- Cache hits → ลด cost, เพิ่ม speed
- Observability → track usage, cost, latency

**ผู้รับผิดชอบ:** AI-Eng (concept), Infra (setup)

---

## 🛠️ วาระที่ 5: Technical Implementation (15 นาที)

**วัตถุประสงค์:** ลงรายละเอียด implementation แต่ละส่วน

### Phase 1: Foundation (Month 1-2)
- [ ] Setup k3s cluster (3 nodes)
- [ ] Deploy Gitea + Gitea Actions
- [ ] Deploy ArgoCD, Harbor, Traefik
- [ ] Deploy LiteLLM + Redis + Langfuse

### Phase 2: Automation (Month 3-4)
- [ ] Integrate Alibaba Qwen API
- [ ] Build auto-doc generation pipeline
- [ ] Implement KM approval workflow
- [ ] Create MCP server template

### Phase 3: Polish (Month 5-6)
- [ ] Build self-service portal
- [ ] Implement governance policies
- [ ] Onboard 3 pilot projects
- [ ] Training & documentation

### MCP Server Auto-Registration:
```python
# ทุก app ต้องมี MCP server
from fastmcp import FastMCP

mcp = FastMCP("my-app")

@mcp.tool()
def query_data(query: str) -> dict:
    """Query data from app"""
    pass

# Auto-register to MCP catalog on deploy
```

### Auto PR & Code Review:
```yaml
# Gitea Actions workflow
name: Auto PR & Review
on:
  push:
    branches: [feature/*]

jobs:
  ai-review:
    runs-on: ubuntu-latest
    steps:
      - name: AI Code Review
        uses: custom/ai-review-action@v1
        with:
          llm_endpoint: "http://litellm:4000/v1"
          model: "qwen-plus"
```

**ผู้รับผิดชอบ:** Dev (implementation), Infra (k3s, Gitea), AI-Eng (LLM, MCP)

---

## 🎯 วาระที่ 6: Next Steps & Action Items (10 นาที)

**วัตถุประสงค์:** สรุปสิ่งที่ต้องทำต่อ และมอบหมายหน้าที่

### Immediate Actions (สัปดาห์หน้า):

**Infra&Security:**
- Setup k3s cluster (test environment)
- Deploy LiteLLM + Redis

**AI-Eng:**
- ทดสอบ Alibaba Qwen API
- สร้าง prototype auto-doc generation

**SA:**
- ออกแบบ wiki schema
- กำหนด KM approval criteria

**Dev:**
- Setup Gitea + Gitea Actions
- สร้าง project template

### Pilot Projects:
- เลือก 3 projects จาก Maintenance (User)
- Onboard ภายใน 2 สัปดาห์

### Success Metrics:
- **Developer Satisfaction** — survey หลังใช้ 1 เดือน
- **Deployment Time** — ลดจาก X ชั่วโมง → Y นาที
- **Documentation Coverage** — 100% ของ projects มี wiki
- **Shadow IT Reduction** — ลด external deployments 50% ใน 3 เดือน

**ผู้รับผิดชอบ:** ทุกทีมรายงานความคืบหน้าทุก 2 สัปดาห์

---

## 📊 สรุปเวลาแต่ละวาระ

| วาระ | หัวข้อ | เวลา | ผู้นำเสนอ |
|------|--------|-------|----------|
| 1 | ปัญหาปัจจุบัน (Pain Points) | 20 นาที | Maintenance (User) |
| 2 | แนวทางแก้ไข (สิ่งที่ควรจะเป็น) | 15 นาที | SA |
| 3 | LLM Wiki + KM Approval | 15 นาที | SA + AI-Eng |
| 4 | LiteLLM + LLM Architecture | 10 นาที | AI-Eng |
| 5 | Technical Implementation | 15 นาที | Dev + Infra |
| 6 | Next Steps & Action Items | 10 นาที | ทุกทีม |
| **รวม** | | **85 นาที** | |

**พักเบรก:** 5 นาที (ระหว่างวาระที่ 3 และ 4)

**รวมเวลาทั้งหมด:** 90 นาที (1 ชั่วโมง 30 นาที)

---

## 👥 บทบาทตามองค์ประชุม

| Role | หน้าที่ในการประชุม |
|------|-------------------|
| **Maintenance (User)** | เล่า pain points, ให้ feedback, เลือก pilot projects |
| **AI-Eng** | อธิบาย LLM integration, LiteLLM, MCP, auto PR |
| **SA** | ออกแบบ architecture, wiki schema, approval workflow |
| **Dev** | อธิบาย implementation, workflow, templates |
| **Infra&Security** | อธิบาย k3s, Gitea, ArgoCD, Vault, RBAC, monitoring |

---

**หมายเหตุ:** นี่คือ **framework** ที่ทีมต้องพัฒนาต่อยอด ไม่ใช่ platform สำเร็จรูป
