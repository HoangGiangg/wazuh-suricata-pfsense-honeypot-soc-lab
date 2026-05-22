import json
from pathlib import Path
from collections import Counter
import streamlit as st

AI_ALERTS = Path("/opt/ai-sec/output/ai_alerts.jsonl")

def load_ai_alerts():
    rows = []
    if not AI_ALERTS.exists():
        return rows

    with AI_ALERTS.open("r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    return rows

def clean_text(val, default=""):
    if val is None:
        return default
    s = str(val).strip()
    if s.lower() == "nan":
        return default
    return s

def get_latest_alert(rows):
    return rows[-1] if rows else None

def get_latest_by_risk(rows, risk):
    matched = [r for r in rows if clean_text(r.get("predicted_risk", "")).lower() == risk.lower()]
    return matched[-1] if matched else None

def explain_risk(alert):
    if not alert:
        return "Hiện chưa có AI alert."

    risk = clean_text(alert.get("predicted_risk", "unknown"))
    module = clean_text(alert.get("module", "unknown"))
    rule_id = clean_text(alert.get("original_rule_id", "unknown"))
    desc = clean_text(alert.get("original_description", ""))
    conf = clean_text(alert.get("confidence", ""))

    lines = []
    lines.append(f"Alert này được xếp loại {risk}.")
    lines.append(f"Nguồn sự kiện: {module}.")
    lines.append(f"Rule gốc: {rule_id}.")
    lines.append(f"Mô tả gốc: {desc}.")
    lines.append(f"Độ tin cậy của mô hình: {conf}.")

    if risk == "critical":
        lines.append("Đây là mức nghiêm trọng cao, thường gắn với malware, tải file nghi vấn hoặc hành vi hậu xâm nhập.")
    elif risk == "high":
        lines.append("Đây là mức nguy hiểm cao, thường gắn với brute-force, web attack hoặc leo thang đặc quyền.")
    elif risk == "medium":
        lines.append("Đây là mức trung bình, thường gắn với truy cập, quét hoặc hành vi nghi vấn ban đầu.")
    else:
        lines.append("Mức độ chưa xác định rõ.")

    return "\n".join(lines)

def format_alert(alert, title="Thông tin alert"):
    if not alert:
        return f"{title}:\nKhông có dữ liệu."

    return (
        f"{title}:\n"
        f"- thời gian: {clean_text(alert.get('timestamp', ''))}\n"
        f"- src_ip: {clean_text(alert.get('src_ip', ''), default='N/A')}\n"
        f"- module: {clean_text(alert.get('module', ''))}\n"
        f"- rule gốc: {clean_text(alert.get('original_rule_id', ''))}\n"
        f"- mô tả: {clean_text(alert.get('original_description', ''))}\n"
        f"- predicted_risk: {clean_text(alert.get('predicted_risk', ''))}\n"
        f"- confidence: {clean_text(alert.get('confidence', ''))}"
    )

def summarize_ip(rows, ip):
    ip = ip.strip()
    matched = [r for r in rows if clean_text(r.get("src_ip", "")) == ip]
    if not matched:
        return f"Không tìm thấy AI alert nào cho IP {ip}."

    risks = Counter(clean_text(r.get("predicted_risk", "unknown")) for r in matched)
    modules = Counter(clean_text(r.get("module", "unknown")) for r in matched)
    rules = Counter(clean_text(r.get("original_rule_id", "unknown")) for r in matched)

    lines = []
    lines.append(f"IP {ip} xuất hiện {len(matched)} lần trong AI alert.")
    lines.append(f"Phân bố mức độ: {dict(risks)}")
    lines.append(f"Module liên quan: {dict(modules)}")
    lines.append(f"Rule gốc nổi bật: {dict(rules.most_common(5))}")
    return "\n".join(lines)

def total_alerts(rows):
    return f"Tổng số AI alert hiện có: {len(rows)}"

def risk_stats(rows):
    risks = Counter(clean_text(r.get("predicted_risk", "unknown")) for r in rows)
    return f"Thống kê mức độ: {dict(risks)}"

def module_stats(rows):
    modules = Counter(clean_text(r.get("module", "unknown")) for r in rows)
    return f"Thống kê module: {dict(modules)}"

def critical_count(rows):
    cnt = sum(1 for r in rows if clean_text(r.get("predicted_risk", "")).lower() == "critical")
    return f"Số alert critical hiện có: {cnt}"

def top_dangerous_ip(rows):
    scored = Counter()
    for r in rows:
        ip = clean_text(r.get("src_ip", ""))
        if not ip:
            continue
        risk = clean_text(r.get("predicted_risk", "")).lower()
        if risk == "critical":
            scored[ip] += 3
        elif risk == "high":
            scored[ip] += 2
        elif risk == "medium":
            scored[ip] += 1

    if not scored:
        return "Không có IP nguồn rõ ràng để đánh giá."

    ip, score = scored.most_common(1)[0]
    return f"IP nguy hiểm nhất hiện tại: {ip} (điểm rủi ro tích lũy: {score})"

def top_5_ips(rows):
    ips = Counter()
    for r in rows:
        ip = clean_text(r.get("src_ip", ""))
        if ip:
            ips[ip] += 1
    if not ips:
        return "Không có IP nguồn rõ ràng."
    return f"Top 5 IP xuất hiện nhiều nhất: {dict(ips.most_common(5))}"

def top_module(rows):
    modules = Counter(clean_text(r.get("module", "unknown")) for r in rows)
    if not modules:
        return "Không có dữ liệu module."
    mod, cnt = modules.most_common(1)[0]
    return f"Module xuất hiện nhiều nhất: {mod} ({cnt} alert)"

def answer_question(question, rows):
    q = question.lower().strip()

    # case cụ thể phải đặt trước case tổng quát
    if "critical mới nhất" in q:
        return format_alert(get_latest_by_risk(rows, "critical"), "Alert critical mới nhất")

    if "high mới nhất" in q:
        return format_alert(get_latest_by_risk(rows, "high"), "Alert high mới nhất")

    if "medium mới nhất" in q:
        return format_alert(get_latest_by_risk(rows, "medium"), "Alert medium mới nhất")

    if "giải thích" in q or "tại sao" in q:
        return explain_risk(get_latest_alert(rows))

    if q.startswith("ip "):
        ip = q.split("ip ", 1)[1].strip()
        return summarize_ip(rows, ip)

    if "ip nào nguy hiểm nhất" in q or "ip nguy hiểm nhất" in q:
        return top_dangerous_ip(rows)

    if "top 5 ip" in q or "top ip" in q:
        return top_5_ips(rows)

    if "module nào nhiều nhất" in q or "module nhiều nhất" in q:
        return top_module(rows)

    if "có bao nhiêu alert critical" in q or ("critical" in q and "bao nhiêu" in q):
        return critical_count(rows)

    if "thống kê mức độ" in q:
        return risk_stats(rows)

    if "thống kê module" in q:
        return module_stats(rows)

    if "có bao nhiêu alert" in q or "tổng số alert" in q:
        return total_alerts(rows)

    if "mới nhất" in q or "latest" in q:
        return format_alert(get_latest_alert(rows), "Alert mới nhất")

    return (
        "Chatbot hiện hỗ trợ:\n"
        "- alert mới nhất là gì\n"
        "- critical mới nhất\n"
        "- high mới nhất\n"
        "- medium mới nhất\n"
        "- giải thích alert này\n"
        "- ip 172.20.10.2\n"
        "- có bao nhiêu alert\n"
        "- có bao nhiêu alert critical\n"
        "- ip nào nguy hiểm nhất\n"
        "- top 5 ip\n"
        "- module nào nhiều nhất\n"
        "- thống kê mức độ\n"
        "- thống kê module"
    )

st.set_page_config(page_title="AI Security Chatbot", layout="wide")
st.title("Chatbot local hỗ trợ phân tích AI alert")

rows = load_ai_alerts()

left, right = st.columns([2, 1])

with left:
    question = st.text_input("Nhập câu hỏi", placeholder="Ví dụ: alert mới nhất là gì")
    if st.button("Gửi"):
        st.text_area("Trả lời", answer_question(question, rows), height=320)

    st.markdown("**Gợi ý câu hỏi**")
    st.code("alert mới nhất là gì")
    st.code("critical mới nhất")
    st.code("high mới nhất")
    st.code("medium mới nhất")
    st.code("giải thích alert này")
    st.code("ip 172.20.10.2")
    st.code("có bao nhiêu alert")
    st.code("có bao nhiêu alert critical")
    st.code("ip nào nguy hiểm nhất")
    st.code("top 5 ip")
    st.code("module nào nhiều nhất")
    st.code("thống kê mức độ")
    st.code("thống kê module")

with right:
    st.subheader("Thông tin nhanh")
    st.write(f"Số AI alert hiện có: {len(rows)}")

    risks = Counter(clean_text(r.get("predicted_risk", "unknown")) for r in rows)
    modules = Counter(clean_text(r.get("module", "unknown")) for r in rows)

    st.markdown("**Phân bố mức độ**")
    st.json(dict(risks))

    st.markdown("**Top module**")
    st.json(dict(modules.most_common(5)))

    latest = get_latest_alert(rows)
    st.markdown("**Alert mới nhất**")
    if latest:
        st.json(latest)
    else:
        st.write("Chưa có dữ liệu.")
