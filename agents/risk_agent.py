def sector_risk(portfolio):
    sector_alloc = portfolio.groupby("sector")["allocation"].sum()
    risky = sector_alloc[sector_alloc > 0.4]
    return risky
