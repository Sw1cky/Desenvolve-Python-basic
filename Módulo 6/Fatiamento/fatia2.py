

menu_sites = ["www.facebook.com", "www.youtube.com", "www.amazon.com", "www.ifood.com", "www.google.com"]

dominios = []
for menu in menu_sites:
    url= menu[4:-4]
    dominios.append(url)

print(dominios)