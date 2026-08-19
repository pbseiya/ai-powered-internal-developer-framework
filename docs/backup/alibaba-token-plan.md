# Alibaba Token Plan — ข้อมูลสำรอง

**หมายเหตุ:** ไฟล์นี้ไม่พูดในการประชุม แต่มี backup ถ้ามีคนถาม

---

## Supported Models (Full List)

| Brand | Models | ความสามารถ |
|-------|--------|------------|
| **Qwen** | qwen3.7-max, qwen3.7-plus, qwen3.6-plus, qwen3.6-flash | Reasoning, text, vision |
| **DeepSeek** | deepseek-v4-pro, deepseek-v4-flash, deepseek-v3.2 | Reasoning, text |
| **Kimi** | kimi-k2.7-code, kimi-k2.6, kimi-k2.5 | Reasoning, text, vision |
| **GLM** | glm-5.2, glm-5.1, glm-5 | Text generation |
| **MiniMax** | MiniMax-M2.5 | Reasoning, text |
| **Image** | qwen-image-2.0, qwen-image-2.0-pro, wan2.7-image, wan2.7-image-pro | Image generation |

---

## Pricing

### Seat Types

| Seat Type | Price | Quota | Use Case |
|-----------|-------|-------|----------|
| Standard | $30/seat/month | 25,000 credits/seat/month | Light AI assistance |
| Pro | $100/seat/month | 100,000 credits/seat/month | Frequent AI coding |
| Max | $200/seat/month | 250,000 credits/seat/month | Heavy AI coding |

### Shared Quota Pack

| Tier | Price | Quota |
|------|-------|-------|
| Shared quota pack | $700/pack | 625,000 credits/pack |

**หมายเหตุ:** แต่ละ pack อายุ 1 เดือน, credits ที่ไม่ใช้จะหายไป

---

## Credit Calculation

### หลักการ: Dynamic Deduction

Credits ถูกคำนวณจาก:
- Model type
- Token count
- Thinking mode
- Tool calls

### ตัวอย่าง: qwen3.6-plus

| Token Type | Count | Credits Consumed |
|------------|-------|------------------|
| Input tokens | 8,349 | 1.67 |
| Cached tokens | 40,794 | 0.82 |
| **รวม** | | **~3.18 credits** |

### Deduction Order

1. หักจาก seat quota ก่อน
2. หมด → หักจาก shared pack (ถ้ามีหลาย pack, หัก pack ที่ใกล้หมดก่อน)
3. หมดทั้งหมด → ระงับบริการจนกว่าจะต่ออายุหรือซื้อ pack ใหม่

---

## Recommendation จาก PPTX

**Approve Budget:** $400/month สำหรับ Premium 2 seats

**เหตุผล:**
- Best value: $0.0008/credit (ถูกที่สุด)
- 500,000 credits/month (250,000 per seat)
- ใช้ 9router + LiteLLM round-robin เพื่อหลีกเลี่ยง rate limits

**Data Privacy:**
- Official guarantee: ไม่เอา conversation data ไป train model
- ตรงตาม enterprise-grade requirements
- มีเอกสารจาก Alibaba Cloud 3 แหล่ง

---

## Architecture: 9router + LiteLLM

```
User Request → 9router (round-robin) → LiteLLM Proxy
                                          ↓
                                    API Key 1 (Seat 1)
                                    API Key 2 (Seat 2)
                                          ↓
                                    Alibaba Qwen API
```

**ประโยชน์:**
- กระจาย load ระหว่าง 2 seats
- หลีกเลี่ยง rate limits
- Serve 10+ users ได้อย่างมีประสิทธิภาพ

---

## ข้อควรระวัง

1. **Region:** Singapore เท่านั้น
2. **Data Privacy:** ไม่ train จาก conversation data
3. **Credits ไม่ carry over** — ใช้ไม่หมดก็หายไป
4. **API Key** — แต่ละ seat มี API key ของตัวเอง, ห้าม share
5. **Cross-border data transfer** — ข้อมูลจะออกจากประเทศ (Singapore region)

---

## Links

- [Token Plan Overview](https://www.alibabacloud.com/help/en/model-studio/token-plan-overview)
- [Token Plan Team Edition FAQ](https://www.alibabacloud.com/help/en/model-studio/token-plan-team-faq)
- [Purchase Page](https://common-buy-intl.alibabacloud.com/token-plan)
- [Console](https://modelstudio.console.alibabacloud.com/?tab=plan#/efm/subscription/token-plan)

---

**Last Updated:** August 2026
