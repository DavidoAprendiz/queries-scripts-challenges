## Laymen classes - Day 2
#### Homework

    1. Choose an Ergo feature/property/technology and prepare small presentation.
    2. Read about the "BearWhale" Saga.
    3. Familirize yourself with the "Pin-Lock-Contract" and understand why it can and has been exploited. 

---
Solutions:

    1. 
    2. https://ergoplatform.org/en/blog/2021-05-13-bearwhale-saga/
        2.1. The "Bearwhale" was frontrunning the oracle price in an attempt to profit at the expense of reserve holders (SigRSV).
        2.2. The "Bearwhale" was taking advantage of this by minting SigUSD early during the "Live Epoch" period of the oracle pool
    3. See "pin_lock.scala"
        3.1. To run the "pin_lock", install Scala (https://www.scala-lang.org/download/)
        3.2. Download the files "pin_lock.scala" and "sbt.build" then run `sbt run` in the same folder
