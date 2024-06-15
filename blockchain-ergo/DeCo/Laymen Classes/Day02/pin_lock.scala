import org.ergoplatform.compiler.ErgoScalaCompiler._
import org.ergoplatform.playgroundenv.utils.ErgoScriptCompiler
import org.ergoplatform.playground._
import org.ergoplatform.Pay2SAddress
import scorex.crypto.hash.Blake2b256

object pin_lock {
  def main(args: Array[String]): Unit = {
  
	  println("#" * 50)
    println("Welcome to the Pin-Lock Example!")
    println("#" * 50)

	  println()
    println("-" * 50)
	  println("Defining and Hashing PIN: ")
    val hashedPin = Blake2b256(scala.io.StdIn.readLine().getBytes())
    //    val hashedPin = Blake2b256("123456789".getBytes())
    println(hashedPin.mkString)
    println("-" * 50)

	  println()
    println("-" * 50)
    println("This is the Smart contract (or Guard Script)")
    println("As defined above, the R4 start to get the hashed PIN that the user inputed and then get the stored on-chain hashed PIN and compare both")
    println("If both are equal, the function returns True and the transactions is successfully added")
	  val pinLockScript =
        s"""
        sigmaProp(INPUTS(0).R4[Coll[Byte]].get == OUTPUTS(0).R4[Coll[Byte]].get)
        """.stripMargin
    val pinLockContract = ErgoScriptCompiler.compile(Map(), pinLockScript)
    println(pinLockContract)
    println("-" * 50)

	  println()
    println("-" * 50)
    println("Creating an address")
    val contractAddress = Pay2SAddress(pinLockContract.ergoTree)
    println("Pin Lock Contract Address: " + contractAddress)
    println("-" * 50)

	  println()
    println("-" * 50)
    println("Creating an test environment to test")
    val blockchainSim = newBlockChainSimulationScenario("PinLock Scenario")
    println(blockchainSim)
    println("-" * 50)

	  println()
    println("-" * 50)
    println("Creating a test Buyer")
    val userParty = blockchainSim.newParty("buyer")
    println(userParty)
    println("-" * 50)

	  println()
    println("-" * 50)
    println("Create variable for 'funds' to add to wallet (value in nanoErgs)")
    val userFunds = 100000000
    println(userFunds)
    println("-" * 50)

	  println()
    println("-" * 50)
    println("Add funds to add to wallet in unspent boxes(value in nanoErgs)")
    userParty.generateUnspentBoxes(toSpend = userFunds)
    userParty.printUnspentAssets()
    println("-" * 50)

	  println()
    println("-" * 50)
    println("Create a box to store the guard script depositing half of user funds to lock")
    val pinLockBox = Box(value = userFunds / 2,
        script = pinLockContract,
        register = R4 -> hashedPin)
    println(pinLockBox)
    println("-" * 50)

	  println()
    println("-" * 50)
    println("Create a transaction, locking the user funds")
    val depositTransaction = Transaction(
        inputs = userParty.selectUnspentBoxes(toSpend = userFunds),
        outputs = List(pinLockBox),
      fee = MinTxFee,
      sendChangeTo = userParty.wallet.getAddress
      )
    println(depositTransaction)
    println("-" * 50)

	  println()
    println("-" * 50)
    println("Signing the TX")
    val depositTransactionSigned = userParty.wallet.sign(depositTransaction)
    blockchainSim.send(depositTransactionSigned)
    println("User funds, after TX")
    userParty.printUnspentAssets()
    println("-" * 50)

	  println()
    println("-" * 50)
    println("Create a box to store the guard script, withdraw half of user funds and pay for Fees")
    val withdrawBox = Box(value = userFunds / 2 - MinTxFee,
        script = contract(userParty.wallet.getAddress.pubKey),
        register = (R4 -> hashedPin))
    println(withdrawBox)
    println("-" * 50)

	  println()
    println("-" * 50)
    println("Create a transaction, unlocking the user funds")
    val withdrawTransaction = Transaction(
        inputs = List(depositTransactionSigned.outputs(0)),
        outputs = List(withdrawBox),
      fee = MinTxFee,
      sendChangeTo = userParty.wallet.getAddress
      )
    println(withdrawTransaction)
    println("-" * 50)

	  println()
    println("-" * 50)
    println("Signing the TX")
    val withdrawTransactionSigned = userParty.wallet.sign(withdrawTransaction)
    blockchainSim.send(withdrawTransactionSigned)
    println("User funds, after TX")
    userParty.printUnspentAssets()
    println("-" * 50)
	
	  println()
    println("#" * 50)
    println(s"The user final balance is the starting balance minus 2 TX fees (0.002 ERG == 2000000 nanoERG)")
    userParty.printUnspentAssets()
    println("#" * 50)
	  println()
  }
}