# 🔐 Blockchain-Based Data Integrity System 

This project is a **decentralized data integrity verification system** that uses:
- 🔒 **Optional AES Encryption**
- 🌐 **IPFS** (via **Pinata** WebApp)
- ⛓️ **Any Blockchain** (For CID registration)  
  > You can store the CID on any blockchain of your choice (I am using Polygon) for immutability and public verification.
- ✅ **Content verification** using blockchain explorer (e.g., PolygonScan / Etherscan)

---

## 📌 Features

- Encrypt any file using AES before sharing (optional)
- Upload to decentralized storage using IPFS via Pinata
- Store and verify IPFS CID on blockchain
- Maintain confidentiality, tamper-proofing, and traceability
- CID can be publicly viewed via blockchain explorer for transparency

---

## 🛠️ Technologies Used

- `Python` for file encryption
- `cryptography` library for AES encryption
- `IPFS` for decentralized file storage
- `Pinata` WebApp for uploading files to IPFS
- `Solidity` for writing smart contracts
- `Remix IDE` for smart contract deployment and interaction (easy for beginners)
- `Polygon Blockchain` for CID registration
- `PolygonScan` (blockchain explorer) for on-chain CID verification

---

## 🧭 Project Workflow

### ✅ Step 1: (Optional) Encrypt File using AES

Use Python's `cryptography` library to encrypt your file before uploading.

    python encrypt.py your_file.txt

⚠️ Save your AES key securely. You’ll need it to decrypt the file later.

## 📤 Step 2: Upload Encrypted File to IPFS using Pinata WebApp

1. Go to [https://app.pinata.cloud](https://app.pinata.cloud)
2. Sign up / log in
3. Navigate to **"Upload" > "File"**
4. Choose your encrypted file (`.enc`) or original file
5. Upload it

After upload, you'll get an **IPFS CID** like: <QmTzQ1dU8m3vC5RQjV5zsdVxzyRzv2Yw9B9oP2C1WnZqhB>


---

## ⛓️ Step 3: Store CID on Blockchain using Smart Contract (via Remix IDE)

> Optional but recommended for transparent, verifiable storage.

### 🔧 Deploying Smart Contract with Remix IDE

1. Visit [https://remix.ethereum.org](https://remix.ethereum.org)
2. Create a new file (e.g., `StoreCID.sol`) and paste the following Solidity code:

and paste .sol code (edit it using your data)

### ⚙️ Remix IDE Steps (Smart Contract Deployment)

1. Go to the **Solidity Compiler** tab:
   - Select version `0.8.x`
   - Click **Compile StoreCID.sol**

2. Go to the **Deploy & Run Transactions** tab:
   - Set environment to **Injected Web3** *(MetaMask must be installed)*
   - Select the appropriate network:
     - ✅ **Polygon Mainnet** → [https://polygonscan.com](https://polygonscan.com)
     - 🧪 **Mumbai Testnet** → [https://mumbai.polygonscan.com](https://mumbai.polygonscan.com)
   - Click **Deploy**

3. After deployment:
   - Expand the deployed contract panel
   - Use `storeCID()` to **submit your IPFS CID**
   - Use `storedCID()` to **read the stored value**

4. Go to the respective blockchain explorer:
   - Search your **contract address**
   - View the stored CID under **Read Contract > storedCID**

🛡️ **Your CID is now permanently and publicly stored on the blockchain!**

---

## 🔍 Step 4: Verify Data Integrity

Use the CID to retrieve the file from any IPFS gateway: https://gateway.pinata.cloud/ipfs/YourCID


- Match the file content or compare hashes to verify integrity  
- If you stored the CID on blockchain:
  - Go to [PolygonScan](https://polygonscan.com) or [Mumbai Explorer](https://mumbai.polygonscan.com)
  - Search your **smart contract address**
  - Call the `storedCID` function to verify the stored CID

---
## Step 5: (Optional) Decrypt Encrypted File
Once the CID is verified and you've downloaded the encrypted file from IPFS, use the following command to decrypt:

    python decrypt.py your_file.txt.enc
    
🔑 Make sure to use the same AES key used during encryption.


## 🔐 Data Security Flow

```text
[Encrypt File] → [Upload to IPFS via Pinata] → [Get CID] → [Store CID on Polygon (optional)] → [Verify CID anytime]

