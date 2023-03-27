from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    # err_key = encrypt_message("frase", "grande")
    # mock_err_key = TypeError("tipo inválido para key")

    # err_message = encrypt_message(234, 2)
    # mock_err_mess = TypeError("tipo inválido para message")

    # with pytest.raises(TypeError) as type_err_key:
    #     raise TypeError("tipo inválido para key")

    # with pytest.raises(TypeError) as type_err_key2:
    #     raise TypeError("tipo inválido para message")

    with pytest.raises(TypeError):
        encrypt_message("frase", "grande")

    with pytest.raises(TypeError):
        encrypt_message(234, 2)

    encry_mess = encrypt_message("frase", 3)
    mock_message = "arf_es"

    encry_mess_bigger = encrypt_message("frase", 5)
    mock_message_bigger = "esarf"

    # assert type_err_key.type is TypeError
    # assert type_err_key2.type is TypeError
    # assert mock_err_key == err_key
    # assert mock_err_mess == err_message
    assert mock_message == encry_mess
    assert mock_message_bigger == encry_mess_bigger
