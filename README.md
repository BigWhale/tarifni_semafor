# Tarifni Semafor – Home Assistant Integration

This custom integration allows you to fetch and display the current and next electricity tariff blocks from [uro.si](https://www.uro.si/o/api/tarifnisemafor/v1/api-docs) in your Home Assistant dashboard.

The integration provides sensors for:
- Current tariff block (as an enum sensor)
- Next tariff block (as an enum sensor)
- Progress of current block (as a numeric sensor)
- Season (as an enum sensor: 1 or 2)

## Features

- Real-time tariff block updates
- Progress tracking of current block
- Season indicator
- Supports Home Assistant dashboards (Lovelace cards)
- Designed for the Slovenian tariff system

---

## Installation

### Option 1: Install via [HACS](https://hacs.xyz/)
1. Go to **HACS > Integrations** in Home Assistant.
2. Click the **"⋮" menu > Custom Repositories**.
3. Add this repository URL:  
   ```
   https://github.com/BigWhale/tarifni_semafor
   ```
   as an **Integration**.
4. Search for **"Tarifni Semafor"** in the HACS integration list and install it.
5. Restart Home Assistant.
6. Add the integration via **Settings > Devices & Services > Add Integration > Tarifni Semafor**.

### Option 2: Manual (Git) Installation
1. Navigate to your Home Assistant configuration directory:
   ```
   /config/custom_components/
   ```
2. Clone this repository:
   ```bash
   git clone https://github.com/BigWhale/tarifni_semafor custom_components/tarifni_semafor
   ```
3. Restart Home Assistant.
4. Add the integration via **Settings > Devices & Services > Add Integration > Tarifni Semafor**.

---

## Configuration

No YAML configuration is required. After installation, configure the integration through the Home Assistant UI.

---

## Sensors Provided

| Sensor                  | Description                       |
|-------------------------|-----------------------------------|
| `sensor.tarifni_current_block` | Current tariff block (enum: 1–5)  |
| `sensor.tarifni_next_block`    | Next tariff block (enum: 1–5)     |
| `sensor.tarifni_block_progress`| Current block progress in percent |
| `sensor.tarifni_season`        | Current season (enum: 1 or 2)     |

Each block sensor also includes the following attributes:
- `block_id`: Current or next block number
- `block_start`: Hour in a day when block starts
- `block_end`: Hour in a day when block ends
- `block_total`: Total number of minutes in the block
- `block_left`:  Number of minutes remaining in the block

---

## Frontend
A custom Lovelace card for visualizing the tariff blocks is [here](https://github.com/BigWhale/tarifni_semafor).

## Credits

Developed for personal use and shared with the community.  
API Source: [Agencija za energijo – URO](https://www.uro.si/aktivni-odjem/tarifni-semafor/)

---

## Support

If you find this integration helpful, consider giving the repo a ⭐ on GitHub or contributing to its development.
