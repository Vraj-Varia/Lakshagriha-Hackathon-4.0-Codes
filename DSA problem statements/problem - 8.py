def generate_cash_envelopes():
    envelopes = [2 ** i for i in range(10)]
    
    if sum(envelopes) > 1000:
        envelopes[-1] -= (sum(envelopes) - 1000)
    
    return envelopes


if __name__ == "__main__":
    envelopes = generate_cash_envelopes()
    print("Envelope values:", envelopes)
    print("Total value:", sum(envelopes))