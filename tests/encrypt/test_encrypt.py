from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("frase", "grande")

    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(234, 2)

    encry_mess = encrypt_message("frase", 3)
    mock_message = "arf_es"

    encry_mess_bigger = encrypt_message("frase", 5)
    mock_message_bigger = "esarf"

    assert mock_message == encry_mess
    assert mock_message_bigger == encry_mess_bigger
