from blockchain.Transaction import Transaction

class Wallet:
    def __init__(self, balance, card_id):
        self.card_id = card_id
        self.balance = balance
        self.public_key = None
        self.private_key = None

    def get_balance(self):
        return self.balance

    def get_card_id(self):
        return self.card_id


# El codigo funciona las tarjetas NO
        
#from smartcard.System import readers
#from smartcard.util import toHexString
#from smartcard.util import HexListToBinString
#
#
#def connect_to_card():
#    # Buscar lectores disponibles
#    reader_list = readers()
#    
#    if not reader_list:
#        print("No se encontraron lectores de tarjetas inteligentes.")
#        return None
#
#    # Seleccionar el primer lector
#    reader = reader_list[0]
#
#    print("Conectándose al lector:", reader)
#
#    try:
#        # Conectar al lector
#        connection = reader.createConnection()
#        connection.connect(protocol=1)
#
#        print("Conectado a la tarjeta:")
#        print("ATR:", toHexString(connection.getATR()))
#
#
#        return connection
#
#    except Exception as e:
#        print("Error al conectar a la tarjeta:", str(e))
#        return None
#
#def send_apdu(connection, apdu):
#    data, sw1, sw2 = connection.transmit(apdu)
#    response = toHexString(data)
#    return response, sw1, sw2
#
## necesito una nueva funcion que mande un apdu y devuelva toda la respuesta independientemente de lo grande que sea
##def send_apdu_full_response(connection, apdu):
##    data, *sw = connection.transmit(apdu)
##    response_data = toHexString(data)
##    status_string = "".join([format(i, '02X') for i in sw])  # Convertir códigos SW a cadena hexadecimal
##    full_response = response_data + status_string
##    return full_response
#
#
#def get_uid(connection):
#    # Enviar el primer APDU (select) APDU: 00 A4 04 00 08   data: A0 00 00 00 03 00 00 00
#    apdu1 = [0x00, 0xA4, 0x04, 0x00, 0x08, 0xA0, 0x00, 0x00, 0x00, 0x03, 0x00, 0x00, 0x00]
#    response, sw1, sw2 = send_apdu(connection, apdu1)
#
#    # Enviar el segundo APDU APDU: 80 50 00 00 08   data: 92 F0 7E B4 1B 5B 18 1C 20
#    apdu2 = [0x80, 0x50, 0x00, 0x00, 0x08, 0x92, 0xF0, 0x7E, 0xB4, 0x1B, 0x5B, 0x18, 0x1C, 0x20]
#    response, sw1, sw2 = send_apdu(connection, apdu2)
#
#    if sw1 == 0x61: 
#        # Enviar comando GET RESPONSE
#        apdu_get_response = [0x00, 0xC0, 0x00, 0x00, sw2]
#        response, sw1, sw2 = send_apdu(connection, apdu_get_response)
#        # De la respuesta quiero los bytes de 5 a 10
#        return response[11:29]
#    else:
#        return None
#
#def check_balance(connection):
#    # Comando APDU para verificar el saldo
#    apdu_check_balance = [0x80, 0x50, 0x00, 0x00, 0x02]
#    response, sw1, sw2 = send_apdu(connection, apdu_check_balance)
#    if sw1 == 0x90 and sw2 == 0x00:
#        # Decodificar la respuesta para obtener el saldo
#        balance = int(response.replace(" ", ""), 16)
#        return balance
#    else:
#        return None
#
#def verify_pin(connection, pin):
#    # Comando APDU para verificar el PIN
#    pin_bytes = bytes.fromhex(pin.replace(" ", ""))
#    apdu_verify_pin = [0x80, 0x20, 0x00, 0x05, len(pin_bytes)] + list(pin_bytes)
#    response, sw1, sw2 = send_apdu(connection, apdu_verify_pin)
#    if sw1 == 0x90 and sw2 == 0x00:
#        return True
#    else:
#        return sw1, sw2
#
#def credit_money(connection, amount):
#    # Comando APDU para acreditar dinero
#    apdu_credit_money = [0x80, 0x30, 0x00, 0x00, 0x01, amount]
#    response, sw1, sw2 = send_apdu(connection, apdu_credit_money)
#    return sw1 == 0x90 and sw2 == 0x00
#
#def debit_money(connection, amount):
#    # Comando APDU para debitar dinero
#    apdu_debit_money = [0x80, 0x40, 0x00, 0x00, 0x01, amount]
#    response, sw1, sw2 = send_apdu(connection, apdu_debit_money)
#    return sw1 == 0x90 and sw2 == 0x00