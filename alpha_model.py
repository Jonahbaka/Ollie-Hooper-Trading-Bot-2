import pandas as pd

def normalise(series, equal_ls=True):
    if equal_ls:
        series -= series.mean()
    sum = series.sum()
    # Test
    return series.apply(lambda x: x/sum)


class ValueAlphaModel():

    def __init__(self):
        pass

    def GenerateAlphaScores(self, algorithm, securities):
        # algorithm.Log(f"Generating alpha scores for {len(securities)} securities...")

        fcf_y = pd.DataFrame.from_records(
            [
                {
                    'symbol': security.Symbol,
                    'fcf_y': security.ValuationRatios.CashReturn
                } for security in securities
            ])

        fcf_y.set_index('symbol', inplace=True)

        fcf_y['alpha_score'] = normalise(fcf_y['fcf_y'], True)

        return fcf_y
