# 🔐 Blockchain-Based Data Integrity System

This project is a **decentralized data integrity verification system** that uses:
- 🔒 **Optional AES Encryption**
- 🌐 **IPFS** (via **Pinata** WebApp)
- ⛓️ **Polygon Blockchain** (optional, for CID registration)
- ✅ **Content verification** using blockchain explorer (PolygonScan)

---

## 📌 Features

- Encrypt any file using AES before sharing (optional)
- Upload to decentralized storage using IPFS via Pinata
- Store and verify IPFS CID on Polygon blockchain (optional)
- Maintain confidentiality, tamper-proofing, and traceability
- CID can be publicly viewed via PolygonScan for transparency

---

## 🛠️ Technologies Used

- `Python` for encryption and automation
- `cryptography` library for AES encryption
- `IPFS` for decentralized file storage
- `Pinata` (WebApp) for uploading and managing files on IPFS
- `Solidity` for smart contract (CID storage)
- `Polygon Blockchain` (Mumbai or Mainnet) for recording CID
- `Web3.py` or `Web3.js` for interacting with blockchain
- `PolygonScan` for CID verification

---

## 🧭 Project Workflow

### ✅ Step 1: (Optional) Encrypt File using AES

Use Python's `cryptography` library to encrypt your file before uploading.

```bash
python encrypt.py your_file.txt
```

> ⚠️ Save your AES key securely. You’ll need it to decrypt the file later.

---

### 📤 Step 2: Upload Encrypted File to IPFS using Pinata WebApp

1. Go to [https://app.pinata.cloud](https://app.pinata.cloud)
2. Sign up / log in
3. Navigate to **"Upload" > "File"**
4. Choose your encrypted file (`.enc`)
5. Upload it

After upload, you'll get an **IPFS CID** like:
```
QmTzQ1dU8m3vC5RQjV5zsdVxzyRzv2Yw9B9oP2C1WnZqhB
```

---

### ⛓️ Step 3: (Optional) Store CID on Polygon using Smart Contract

If you want to **record your CID on blockchain**:

1. Write a simple Solidity contract:
```solidity
string public storedCID;

function storeCID(string memory _cid) public {
    storedCID = _cid;
}
```

2. Deploy using Hardhat or Web3.py to Polygon (Mumbai or Mainnet)

3. After deployment, call the function `storeCID()` with your Pinata CID

4. View it on [PolygonScan](https://mumbai.polygonscan.com/) or [https://polygonscan.com](https://polygonscan.com)

---

### 🔍 Step 4: Verify Integrity

- Use the CID to retrieve the file from any IPFS gateway:
  ```
  https://gateway.pinata.cloud/ipfs/YourCID
  ```

- Match the file hash or content to verify data hasn't changed

- If CID is stored on Polygon:
  - Visit PolygonScan
  - Search for your contract
  - Confirm that the CID matches what you uploaded

---

## 🔐 Data Security Flow

```text
[Encrypt File] → [Upload to IPFS via Pinata] → [Get CID] → [Store CID on Polygon (optional)] → [Verify CID anytime]
```

---

## 🔮 Future Enhancements

- Encrypted file preview/decryption in web UI
- QR code generation for stored CID
- IPNS or ENS integration for human-readable links
- Role-based access for CID storage
- CID auto-store with frontend and wallet connection

---

## 📁 Folder Structure (if you add code)

```
/blockchain-integrity-project
│
├── encrypt.py              # AES encryption script
├── decrypt.py              # Decryption script
├── deploy_contract.py      # Script to deploy contract
├── contract.sol            # Solidity smart contract
├── README.md               # Project documentation
└── ...                     # Other supporting files
```

---

## 📜 License

This project is released under the **MIT License** and is open for academic and learning purposes.

---

## 👨‍💻 Created by

**Aditya Patil (Aadiii / Aadu)**  
Feel free to contribute or fork the repo!
