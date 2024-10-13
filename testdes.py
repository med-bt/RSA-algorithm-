import DES
import time
import matplotlib.pyplot as plt
message = '''
Qu'est-ce que le Lorem Ipsum?
Le Lorem Ipsum est simplement du faux texte employé dans la composition et la mise en page avant impression. Le Lorem Ipsum est le faux texte standard de l'imprimerie depuis les années 1500, quand un imprimeur anonyme assembla ensemble des morceaux de texte pour réaliser un livre spécimen de polices de texte. Il n'a pas fait que survivre cinq siècles, mais s'est aussi adapté à la bureautique informatique, sans que son contenu n'en soit modifié. Il a été popularisé dans les années 1960 grâce à la vente de feuilles Letraset contenant des passages du Lorem Ipsum, et, plus récemment, par son inclusion dans des applications de mise en page de texte, comme Aldus PageMaker.
On sait depuis longtemps que travailler avec du texte lisible et contenant du sens est source de distractions, et empêche de se concentrer sur la mise en page elle-même. L'avantage du Lorem Ipsum sur un texte générique comme 'Du texte. Du texte. Du texte.' est qu'il possède une distribution de lettres plus ou moins normale, et en tout cas comparable avec celle du français standard. De nombreuses suites logicielles de mise en page ou éditeurs de sites Web ont fait du Lorem Ipsum leur faux texte par défaut, et une recherche pour 'Lorem Ipsum' vous conduira vers de nombreux sites qui n'en sont encore qu'à leur phase de construction. Plusieurs versions sont apparues avec le temps, parfois par accident, souvent intentionnellement (histoire d'y rajouter de petits clins d'oeil, voire des phrases embarassantes).
On sait depuis longtemps que travailler avec du texte lisible et contenant du sens est source de distractions, et empêche de se concentrer sur la mise en page elle-même. L'avantage du Lorem Ipsum sur un texte générique comme 'Du texte. Du texte. Du texte.' est qu'il possède une distribution de lettres plus ou moins normale, et en tout cas comparable avec celle du français standard. De nombreuses suites logicielles de mise en page ou éditeurs de sites Web ont fait du Lorem Ipsum leur faux texte par défaut, et une recherche pour 'Lorem Ipsum' vous conduira vers de nombreux sites qui n'en sont encore qu'à leur phase de construction. Plusieurs versions sont apparues avec le temps, parfois par accident, souvent intentionnellement (histoire d'y rajouter de petits clins d'oeil, voire des phrases embarassantes).
On sait depuis longtemps que travailler avec du texte lisible et contenant du sens est source de distractions, et empêche de se concentrer sur la mise en page elle-même. L'avantage du Lorem Ipsum sur un texte générique comme 'Du texte. Du texte. Du texte.' est qu'il possède une distribution de lettres plus ou moins normale, et en tout cas comparable avec celle du français standard. De nombreuses suites logicielles de mise en page ou éditeurs de sites Web ont fait du Lorem Ipsum leur faux texte par défaut, et une recherche pour 'Lorem Ipsum' vous conduira vers de nombreux sites qui n'en sont encore qu'à leur phase de construction. Plusieurs versions sont apparues avec le temps, parfois par accident, souvent intentionnellement (histoire d'y rajouter de petits clins d'oeil, voire des phrases embarassantes).
'''
encryption_times = []
decryption_times = []
start_time = time.time() 
encrypted_ecb = DES.encrypt_ecb(message)
encryption_ecb_time = time.time() - start_time
print("Encrypted (ECB):", encrypted_ecb , " time taken : "+ str(encryption_ecb_time))
start_time = time.time() 
decrypted_ecb = DES.decrypt_ecb(encrypted_ecb)
decryption_ecb_time = time.time() - start_time
print("Decrypted (ECB):", decrypted_ecb ," time taken  : "+ str(decryption_ecb_time))

start_time = time.time() 
encrypted_cbc = DES.encrypt_cbc(message)
encryption_cbc_time = time.time() - start_time
print("Encrypted (CBC):", encrypted_cbc," time taken : "+ str(encryption_cbc_time))

start_time = time.time()
decrypted_cbc = DES.decrypt_cbc(encrypted_cbc)
decryption_cbc_time = time.time() - start_time
print("Decrypted (CBC):", decrypted_cbc," time taken : ", str(decryption_cbc_time))

modes = ['ECB Encryption', 'ECB Decryption', 'CBC Encryption', 'CBC Decryption']
times = [encryption_ecb_time, decryption_ecb_time, encryption_cbc_time, decryption_cbc_time]

plt.figure(figsize=(10, 5))
plt.bar(modes, times, color=['blue', 'orange', 'green', 'red'])
plt.ylabel('Time (seconds)')
plt.title('DES Encryption and Decryption Times')
plt.grid(axis='y')
plt.show()