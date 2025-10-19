from termcolorx import TermColorX as tc, LoggerColor, Gradient, Animation, PlatformSupport

# Aktifkan ANSI
PlatformSupport.enable_ansi()

print(tc.bold(tc.red("=== DEMO TERMOLORX v2.0.0 ===")))
print(tc.green(str(PlatformSupport.info())))

# Pewarnaan Dasar
print(tc.colorize("Merah tebal dengan latar kuning", fg="red", bg="yellow", style="bold"))
print(tc.rgb("Custom RGB warna ungu", 160, 32, 240))
print(tc.color256("256 warna kode 45", 45))
print(Gradient.rainbow("Teks Gradien Pelangi 🌈"))

# Logger
log = LoggerColor("DemoLogger", log_file="demo_log.txt")
log.info("Inisialisasi sistem...")
log.success("Koneksi berhasil!")
log.warning("Memori mulai penuh...")
log.error("File tidak ditemukan!")
log.critical("SISTEM MATI!")

# Animasi
Animation.typing("Menjalankan animasi teks berjalan...", color="cyan")
Animation.spinner(duration=3)
Animation.multiline_typing([
    "Baris pertama animasi...",
    "Baris kedua animasi...",
    "Baris ketiga animasi..."
])