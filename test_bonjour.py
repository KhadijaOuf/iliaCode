from bonjour import saluer
def test_saluer_khadija():
     assert saluer("Khadija") == "Bonjour Khadija" 
     
def test_saluer_vide(): 
     assert saluer("") == "Bonjour "