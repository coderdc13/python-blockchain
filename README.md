# python-blockchain
# Python Wallet



The goal of this assignment is for the student-author (me, Franklin Bueno) to compose a wallet for the trade of both test bitcoin and test ethereum. This wallet is to be made with the wallet from a GitHub source and executed with ethereum geth program. The transactions of the wallet are to be recorded in different tracking programs. Also, the required packages are given in the requirements.txt file.

In terms of the wallet itself, the wallet itself is a creation from https://github.com/dan-da/hd-wallet-derive. This wallet is built with Python script and the software was loaded onto MS VSCode. Loading the wallet from a .py file shows several functions: derive_wallets, priv_key_to_account, create_tx, send_tx. With these functions, the user is supposed to be able to send testnet bitcoin and ethereum from the command line. Also, the user, from the command line, is supposed to be able to see the testnet bitcoin and ethereum accounts. The user is supposed to provide parameters of the kind of coin (BTC or ETH), the intended sending and recipient addresses, and the amount of BTC or ETH. Then the user is supposed to enter the parameters, execute the function, and then observe the exchanges on an online software application that tracks bitcoin and ethereum transactions.








## BTC-TEST Wallet

This section aims to pair the screenshots (provided below) with the corresponding code and command line commands for the testing of the bitcoin functionality of the wallet.


![text](/Screenshots/Screenshot%20(1973).png)

The figure above corresponds to the correct test of the installation of the wallet. A number of programs are needed to load the wallet, including PHP. This screen shows that the wallet was downloaded and also the large Python dictionary shows the dictionaries and lists for the BTCTEST and ETH wallet.


![text](/Screenshots/Screenshot%20(1974).png)


The figure above shows additional data being printed from the wallet.py program.


![text](/Screenshots/Screenshot%20(1975).png)


For the BTCTEST (as with the ETH), the needed functions are from the wallet.py file: derive_wallets, priv_key_to_account, create_tx, send_tx. In the illustrated directory, the program is called by entering a specific command: python wallet.py.



![text](/Screenshots/Screenshot%20(1976).png)





![text](/Screenshots/Screenshot%20(1977).png)






![text](/Screenshots/Screenshot%20(1978).png)



The three images above show the successful transfer of the test bitcoin based solely on the use of the function, and no direct transfer through online softare.

![text](/Screenshots/Screenshot%20(1979).png)



The image directly above shows the student-author's attempt to separate out the functions with the variables starter and middler.

![text](/Screenshots/Screenshot%20(1980).png)






![text](/Screenshots/Screenshot%20(1981).png)






![text](/Screenshots/Screenshot%20(1982).png)





![text](/Screenshots/Screenshot%20(1983).png)





![text](/Screenshots/Screenshot%20(1984).png)



The rest of the images above show earlier unsuccessful attempts at the bitcoin transaction, but the final bitcoin transaction was successful and documented through the online service (above).


## ETH Wallet


This section aims to pair the screenshots (provided below) with the corresponding code and command line commands for the testing of the ethereum functionality of the wallet.





![text](/Screenshots/Screenshot%20(2018).png)


The figure above corresponds to the correct test of the installation of the wallet. A number of programs are needed to load the wallet, including PHP. This screen shows that the wallet was downloaded and also the large Python dictionary shows the dictionaries and lists for the BTCTEST and ETH wallet.



![text](/Screenshots/Screenshot%20(2019).png)






![text](/Screenshots/Screenshot%20(2021).png)



For the BTCTEST (as with the ETH), the needed functions are from the wallet.py file: derive_wallets, priv_key_to_account, create_tx, send_tx. In the illustrated directory, the program is called by entering a specific command: python wallet.py. The two images above reflect attempts at trying to access those functions for an exchange of ETH.




![text](/Screenshots/Screenshot%20(2025).png)







![text](/Screenshots/Screenshot%20(2026).png)







![text](/Screenshots/Screenshot%20(2027).png)





![text](/Screenshots/Screenshot%20(2028).png)







![text](/Screenshots/Screenshot%20(2029).png)






![text](/Screenshots/Screenshot%20(2030).png)


The rest of the images reflect the attempts of the student-author to complete the transaction for ETH. As a result of the persistent errors thrown, in an extended office-hours session, the student-author was advised to use the additional command of --minerthreads 1. This command only highlighted discrepancies in the actual nodes of the blockchain (both node1 and node2, whose processes are both shown above).



Ultimately, student-author was instructed to submit the final attempt at the ethereum wallet as-is. The student-author is continuing to seek a solution to this challenge. Furthermore, the student-author will notify the Instructor Corps as soon as he solves this specific challenge. The student-author is going to redo the entire program, including geth installation, just as for basic python. From the extended office-hours session, it seemed that the problem was in the blockchain. Also, the student-author is going to conduct a comprehensive internet search for this error and will remedy based on the provided solutions and recommendations..





(NB - At least 99.9999% of the original ideas for this work are from the given course materials, Instructors GS, AN, and KS, and the Tutor, Ms. LT ... also, because of the shared subject matter between the third project of Group Two and this assignment, the student-author saw the homework material and leveraged the homework material of Group Two teammate, Mr. E___ "T___" McM___ ...)
