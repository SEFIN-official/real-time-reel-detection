# Dataset Description

## Overview
Our dataset combines reel and non-reel network traffic features extracted from real packet captures and synthetic traffic. The goal is to distinguish real-time streaming (reel) traffic from other types.

## Data Sources
- Reel and non-reel PCAP files captured from simulated and live environments.
- Synthetic traffic data used for robustness and augmentation.

## Feature Engineering
Extracted features include:
- `packet_size`: size of network packets
- `duration`: time difference between packets
- `protocol_code`: encoded protocol type (TCP/UDP/HTTP)
- `network_code`: categorical network quality indicator

## Dataset Statistics
- Total samples: Approx. 42,000 (combined)
- Class distribution: 66% non-reel, 34% reel
- Duration feature proved most important for classification.

## Data Usage
- Data was stratified and split into train and test sets to ensure balanced evaluation.
