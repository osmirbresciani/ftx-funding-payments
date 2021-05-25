def sum_funding(json_result):
    # json_funding = [{'id': 355273230, 'future': 'STEP-PERP', 'payment': -1.23850545, 'time': '2021-05-25T00:00:00+00:00', 'rate': -0.000861}, {'id': 355205706, 'future': 'STEP-PERP', 'payment': -1.2470705, 'time': '2021-05-24T23:00:00+00:00', 'rate': -0.000865}]
    payment = 0
    for payments in range(len(json_result)):
        payment += json_result[payments]["payment"]
    long_position = payment * (-1)
    short_position = payment
    return {"long_payment": str(long_position), "short_payment": str(short_position)}


# if __name__ == '__main__':
#     sum_funding()
