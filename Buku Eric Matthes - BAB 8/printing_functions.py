def print_models(desain_belum_dicetak, model_selesai):
    """
    Simulasikan pencetakan tiap desain sampai habis.
    Pindahkan tiap desain ke model_selesai setelah dicetak.
    """
    while desain_belum_dicetak:
        desain_saat_ini = desain_belum_dicetak.pop()
        print(f"Mencetak model: {desain_saat_ini}")
        model_selesai.append(desain_saat_ini)


def show_completed_models(model_selesai):
    """Tampilkan semua model yang sudah dicetak."""
    print("\nModel berikut sudah selesai dicetak:")
    for model in model_selesai:
        print(model)