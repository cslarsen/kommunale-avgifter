"""
kommunale avgifter per 2021

https://www.sandnes.kommune.no/teknisk-og-eiendom/vann-avlop-og-renovasjon/kommunale-avgifter/
"""

# størrelse bolig
kvm = 107
moms = 1.25

# 2021: uten vannmåler
# priser tatt (uten moms) fra nettsiden over
post = {
    "forbruk vann": kvm * 11.00,  # Eks mva
    "forbruk avløp": kvm * 16.60,  # Eks mva
    "abbonnement vann": kvm * 4.20,  # Eks mva
    "abbonnement avløp": kvm * 7.60,  # Eks mva
    "grunngebyr": 785 / moms,  # Oppgitt uten mva
    "restavfall 240l": 2826 / moms,  # Oppgitt uten mva
    "papiravfall": 393 / moms,  # Oppgitt uten mva
    "bioavfall": 1178 / moms,  # Oppgitt uten mva
}

# Under stemmer god med 2020 og regningen jeg fikk
post_2020 = {
    "forbruk vann": kvm * 9,
    "forbruk avløp": kvm * 16,
    "abbonnement vann": kvm * 4.20,
    "abbonnement avløp": kvm * 7.60,
    "grunngebyr": 600,
    "restavfall 240l": 1890,
    "papiravfall": 300,
    "bioavfall": 840,
}

total = sum(post.values())
post["total per år"] = total
post["total per halvår"] = total / 2

print("Kvadratmeter bolig:", kvm)
print("Momssats: %.0f%%" % (100.0 * (moms - 1)))
print("")

width = max(len(x) for x in post.keys())

for navn, pris in post.items():
    if navn == "total per år":
        print("=" * (width + 9))
    print("%-*s" % (width, navn.capitalize()),
          "%8.2f" % (pris * moms))
