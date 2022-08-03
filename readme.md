# Tulip Protocol Overview and Dashboard

The [Tulip Protocol](https://tulip.garden) Dashboard will provide the Tulip DAO with a comprehensive overview of the protocol’s core KPIs across its different product offerings. 

[Bounty](https://app.realms.today/dao/413KSeuFUBSWDzfjU9BBqBAWYKmoR8mncrhV84WcGNAk/proposal/2XAVTwsMJtS9NVLtpzp1VYkbHauvLroijzUFQdDUA7YK)

## Team
github: [@0xBlackfish](https://github.com/0xBlackFish) | twitter: [0xBlackfish](https://twitter.com/0xBlackFish)

github: [@amarante-codes](https://github.com/amarante-codes) | twitter: [@AmaranteCodes](https://twitter.com/AmaranteCodes)

## Dashboard Metrics

### P&L

* Revenue / Interest Generated
* Value returned to users/wallets

### User / Wallet Activity

* Wallet Growth
* Deposit Growth
* Wallet/User Engagement
* Wallet/User Retention
* Net Dollar Retention
* Wallet LTV
* DAWs (Daily Active Wallets)
* DAWs/WAWs Ratio

### Concentration Risk

* Distribution of funds within products across different pools / farms
* Distribution of funds within pools/farms themselves

### Marketing

* Acquisition Funnel Conversion Rates
* Visits → Connect Wallet → Engage w/ Tulip
* Customer Acquistion Cost (CAC)
* Performance of Individual Marketing Campaigns

## Scope
Any data infrastructure-related work that is required to hydrate the dashboard is in scope. Blackfish/Amarante will work with the Tulip team if they already have existing data assets or providers. If not, Blackfish/Amarante will help facilitate relationships with on-chain data providers for Solana such as Dune, Solana FM, ZettaBlocks, etc.

## Dashboard Infrastructure

Dashboard will be built using Dash. All deliverables and the final dashboard will be open source and public facing.

### Data Architecture

The Dashboard will be served files stored in a Google Cloud Storage bucket. This bucket will be public so the dashboard and other members of the community can interact with the Tulip dashboard data as desired.

The bucket will be hyrdated by a data pump service that will be scheduled to create flow by pulling from data pipelines provided by the Growth Vector API.
