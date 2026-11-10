# Portal ANTIGO (Streamlit Cloud) — só avisa o novo endereço e redireciona.
import streamlit as st
import streamlit.components.v1 as components

NOVO = "https://www.3dguide.com.br"

st.set_page_config(page_title="3D Guide — Portal de Pedidos", page_icon="🦷",
                   layout="centered")
st.markdown("""
<div style="text-align:center;padding:2.2rem 1rem;border-radius:16px;
background:linear-gradient(135deg,#0e4d66,#1a6b8a);color:#fff;margin-top:1rem">
  <div style="font-size:2.4rem">🦷</div>
  <h2 style="color:#fff;margin:.4rem 0">O Portal de Pedidos mudou de endereço</h2>
  <p style="font-size:1.05rem;margin:0">Este endereço antigo não recebe mais arquivos.<br>
  Faça seu pedido pelo novo portal:</p>
  <p style="font-size:1.35rem;font-weight:700;margin:.8rem 0 0">www.3dguide.com.br</p>
</div>""", unsafe_allow_html=True)
st.write("")
st.link_button("➡️ Abrir o novo portal", NOVO, type="primary", use_container_width=True)
st.caption("Se você já tinha enviado arquivos por este endereço, envie-os novamente "
           "pelo novo portal. Dúvidas: WhatsApp (27) 99730-0521.")
# Tenta redirecionar sozinho (se o navegador bloquear, fica o botão acima)
components.html(f"<script>try{{window.top.location.href='{NOVO}';}}catch(e){{}}</script>",
                height=0)
