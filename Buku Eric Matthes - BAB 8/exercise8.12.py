def buat_sandwich(*isian):
    """Tampilkan ringkasan sandwich yang dipesan."""
    print("\nMembuat sandwich dengan isian berikut:")
    for item in isian:
        print(f"- {item}")


buat_sandwich("tuna")
buat_sandwich("ayam", "keju")
buat_sandwich("telur", "selada", "tomat", "mayones")