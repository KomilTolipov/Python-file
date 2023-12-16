from datetime import datetime

# Joriy vaqtni olish
joriy_vaqt=datetime.now()
print(joriy_vaqt)

# %a hafta kuni (qisqa)
hafta_kuni_qisqa=joriy_vaqt.strftime("%a")
print(f"Hafta kuni qisqa:{hafta_kuni_qisqa}")

# %A–hafta kuni (to’liq)
hafta_kuni_tolik=joriy_vaqt.strftime("%A")
print(f"Hafta kuni toliq: {hafta_kuni_tolik}")

# %w-hafta kuni (raqam shaklida)
hafta_kuni_raqam=joriy_vaqt.strftime("%w")
print(f"Hafta kuni raqam shaklida:{hafta_kuni_raqam}")

# %d–oyning sanasi
oy_sanasi=joriy_vaqt.strftime("%d")
print(f"Oyning sanasi:{oy_sanasi}")

# %b–oy nomi (qisqa)
oy_nomi_qisqa=joriy_vaqt.strftime("%b")
print(f"Oy nomi qisqa:{oy_nomi_qisqa}")

# %B–oy nomi (to’liq)
oy_nomi_tolik = joriy_vaqt.strftime("%B")
print(f"Oy nomi toliq: {oy_nomi_tolik}")

# %m–oy (raqam ko’rinishida)
oy_raqami=joriy_vaqt.strftime("%m")
print(f"Oy raqam korinishida:{oy_raqami}")

# %y–yil (qisqa)
yil_qisqa=joriy_vaqt.strftime("%y")
print(f"Yil qisqa:{yil_qisqa}")

# %Y–yil (to’liq)
yil_tolik=joriy_vaqt.strftime("%Y")
print(f"Yil toliq:{yil_tolik}")

# %H–soat (00-23)
soat_24=joriy_vaqt.strftime("%H")
print(f"Soat (00-23):{soat_24}")

# %I–soat (00-12)
soat_12=joriy_vaqt.strftime("%I")
print(f"Soat (00-12):{soat_12}")

# %p–kun vaqti (AM/PM)
kun_vaqti=joriy_vaqt.strftime("%p")
print(f"Kun vaqti (AM/PM):{kun_vaqti}")

# %M–minut (00-59)
minut=joriy_vaqt.strftime("%M")
print(f"Minut (00-59):{minut}")

# %S–sekund (00-59)
sekund=joriy_vaqt.strftime("%S")
print(f"Sekund (00-59):{sekund}")

# %j–yildagi kun raqami (001-366)
yildagi_kun_raqami=joriy_vaqt.strftime("%j")
print(f"Yildagi kun raqami (001-366):{yildagi_kun_raqami}")

# %U – yildagi hafta raqami, Yakshanba birinchi kun sifatida (00-53)
hafta_raqami_yakshanba=joriy_vaqt.strftime("%U")
print(f"Yildagi hafta raqami Yakshanba birinchi kun sifatida :{hafta_raqami_yakshanba}")

# %W – yildagi hafta raqami, Dushanba birinchi kun sifatida (00-53)
hafta_raqami_dushanba=joriy_vaqt.strftime("%W")
print(f"yildagi hafta raqami dushanba birinchi kun sifatida :{hafta_raqami_dushanba}")

# %c – mahalliy sana va vaqt
mahalliy_sana_va_vaqt=joriy_vaqt.strftime("%c")
print(f"Mahalliy sana va vaqt:{mahalliy_sana_va_vaqt}")

# %x – mahalliy sana
mahalliy_sana=joriy_vaqt.strftime("%x")
print(f"Mahalliy sana:{mahalliy_sana}")

# %X – mahalliy vaqt
mahalliy_vaqt=joriy_vaqt.strftime("%X")
print(f"Mahalliy vaqt:{mahalliy_vaqt}")

