import emoji

frase = input("Digite sua frase é coloque nela um emoji: ")

emojis_para_uso= {
    ":red_heart:": "❤️",
    ":thumbs_up:": "👍",
    ":thinking_face:": "🤔",
    ":partying_face:": "🥳"
}


print("Emojis :")
for cod, emoji_codigo in emojis_para_uso.items():
    print(f"{emoji_codigo} - {cod}")

frase_com_emoji= emoji.emojize(frase, aliases=emojis_para_uso)

print("sua fraze com emojis:")
print(frase_com_emoji)