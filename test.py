def invoice(inputs, discount, service_charge):
    total = 0
    for i in inputs:
        total += i[0]*i[1]
    sub_total = total - (total * discount / 100)
    return round(sub_total - (service_charge * sub_total / 100), 2)


liste = [(310, 1), (300, 1)]

print(invoice(liste, 15, 1))