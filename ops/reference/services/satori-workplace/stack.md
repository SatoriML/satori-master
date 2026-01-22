# Teknisk stack

> Referens: [european-alternatives.eu](https://european-alternatives.eu/) - katalog över europeiska alternativ till Big Tech

## Översikt

| Funktion        | Microsoft           | satori-workplace          | Andrahandsval                   |
| --------------- | ------------------- | ------------------------- | ------------------------------- |
| Infrastruktur   | Azure               | Elastx 🇸🇪               | Glesys 🇸🇪                     |
| Hårdvara PC     | Dell / HP / Lenovo  | Slimbook 🇪🇸             | TUXEDO 🇩🇪                     |
| Hårdvara Mobil  | iPhone / Samsung    | Jolla / Sony Xperia       | Fairphone 🇳🇱                  |
| Klient-OS       | Windows             | Linux Mint Cinnamon       | -                               |
| Mobil-OS        | iOS / Android       | Sailfish OS 🇫🇮          | /e/OS 🇫🇷                      |
| Server-OS       | Windows Server      | RHEL                      | -                               |
| Identitet       | Active Directory    | FreeIPA                   | -                               |
| Enhetshantering | Intune              | FleetDM On-prem Usa..     | -                               |
| Intern chat     | Teams               | Mattermost/Vroff          | Nextcloud Talk                  |
| AI-assistent    | Copilot             | satori-chat               | -                               |
| E-post          | Outlook/Exchange    | Proton Mail 🇨🇭          | Infomaniak 🇨🇭 / Nextcloud / OpenDesk 🇩🇪 |
| Kalender        | Outlook             | Proton Calendar 🇨🇭      | Infomaniak 🇨🇭 / Nextcloud / OpenDesk 🇩🇪 |
| Kontorssvit     | Office 365          | Proton Docs 🇨🇭          | Infomaniak 🇨🇭 / Nextcloud / OpenDesk 🇩🇪 |
| Fillagring      | SharePoint/OneDrive | Proton Drive 🇨🇭         | Infomaniak 🇨🇭 / Nextcloud / OpenDesk 🇩🇪 |
| VPN             | -                   | Proton VPN 🇨🇭           | Mullvad 🇸🇪                    |
| Lösenord        | -                   | Proton Pass 🇨🇭          | Vaultwarden (self-hosted)       |
| Videokonferens  | Teams               | Proton Meet 🇨🇭          | Jitsi (self-hosted)             |
| 2FA             | MS Authenticator    | Proton Authenticator 🇨🇭 | Aegis (lokal)                   |
| Nätverk         | Cisco / Ubiquiti    | MikroTik 🇱🇻             | Sophos 🇬🇧                      |

## Arkitektur

```
┌─────────────────────────────────────────────────────────────┐
│              KLIENTER (Slimbook / Jolla)                    │
├─────────────────────────────────────────────────────────────┤
│  Linux Mint ─── FreeIPA ─── Mattermost ─── satori-chat     │
│       │            │                                        │
│  Sailfish OS ─────┘            │                           │
│       │                        │                            │
│       └──── FleetDM (enhetshantering) ────┘                │
└─────────────────────────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│              INFRASTRUKTUR (Elastx / Glesys) 🇸🇪            │
├─────────────────────────────────────────────────────────────┤
│  RHEL │ Kubernetes │ FreeIPA │ Mattermost │ satori-chat    │
└─────────────────────────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                   PROTON (Schweiz) 🇨🇭                      │
├─────────────────────────────────────────────────────────────┤
│  Mail │ Calendar │ Drive │ Docs │ VPN │ Pass │ Meet        │
└─────────────────────────────────────────────────────────────┘
```

## Komponentval

### Infrastruktur (hosting)

#### Elastx 🇸🇪
- Svenskt molnbolag, Stockholm
- Kubernetes-fokuserat (Compliant Kubernetes)
- ISO 27001 certifierat
- GDPR-compliant
- Hållbarhetsfokus (100% förnybar energi)

#### Glesys 🇸🇪
- Svenskt hostingbolag sedan 1999
- Datacenter i Stockholm, Falkenberg
- VPS, dedikerade servrar, objektlagring
- VMware Cloud Director
- Bra för traditionell VM-hosting

### Hårdvara

#### Slimbook
- 🇪🇸 Spanskt företag - EU-jurisdiktion
- Linux-först design (ingen Windows-skatt)
- Coreboot-stöd på vissa modeller
- Laptops, desktops, mini-PCs
- Direktsupport för Linux

#### Jolla / Sony Xperia
- Jolla-telefoner: Native Sailfish
- Sony Xperia: Flashbar med Sailfish
- Enterprise MDM-stöd

### Nätverksutrustning

#### MikroTik 🇱🇻
- Lettiskt företag
- RouterOS - kraftfullt och flexibelt
- Routrar, switchar, accesspunkter
- Prisvärt enterprise-alternativ

#### Sophos 🇬🇧
- Brittiskt företag (Oxfordshire)
- UTM/nästa-gen brandväggar
- XG Firewall, accesspunkter
- Central molnhantering

### Self-hosted infrastruktur

#### Linux Mint Cinnamon
- Användarvänligt för Windows-flyktingar
- Stabil LTS-bas (Ubuntu)
- Minimal inlärningskurva

#### Sailfish OS (Jolla)
- 🇫🇮 Finskt företag - EU-jurisdiktion
- Äkta Linux-kärna (inte Android)
- MDM-stöd för enterprise
- Android app-kompatibilitet (valfritt)
- Används av myndigheter (Ryssland, Latinamerika)
- Hardware: Jolla-telefoner eller Sony Xperia (flash)

#### RHEL
- Enterprise-support
- Säkerhetscertifieringar
- 10 års support

#### FreeIPA
- Full AD-ersättning
- Kerberos + LDAP
- Integrerat med Linux

#### FleetDM
- Öppen källkod MDM
- osquery-baserad endpoint visibility
- Patch management
- Compliance queries

#### Mattermost
- Self-hosted
- Slack-liknande UX
- Enterprise-features

#### satori-chat
- Egen AI-assistent
- Lokal inferens möjlig
- Ingen data till tredje part

### Proton-sviten (managed)

Schweizisk leverantör med E2E-kryptering:
- **Proton Mail** - Krypterad e-post
- **Proton Calendar** - Integrerad kalender
- **Proton Drive** - Molnlagring
- **Proton Docs/Sheets** - Kontorssvit
- **Proton VPN** - Säker fjärråtkomst
- **Proton Pass** - Lösenordshantering
- **Proton Meet** - Videokonferens
- **Proton Authenticator** - 2FA

## Compliance & jurisdiktion

### Schweiz (Proton)
| Aspekt | Status |
|--------|--------|
| GDPR | "Adequacy decision" från EU |
| CLOUD Act | Ej tillämplig |
| Dataskyddslag | nDSG 2023 (GDPR-liknande) |

**OBS:** Schweiz är inte EU/EEA. För offentlig sektor med strikta krav på
EU-datalagring kan Proton vara problematiskt vid upphandling.

### Rekommendation per kundtyp

| Kundtyp | Proton OK? | Rekommendation |
|---------|------------|----------------|
| Privat sektor | ✅ Ja | Proton default |
| Offentlig sektor (standard) | ⚠️ Kanske | Juridisk bedömning krävs |
| Offentlig sektor (känslig) | ❌ Nej | EU-alternativ / self-hosted |
| Säkerhetsklass | ❌ Nej | 100% self-hosted |

### Andrahandsval (100% EU/self-hosted)

När Schweiz-lösningar (Proton) inte är tillåtna:

| Funktion | Alternativ | Jurisdiktion |
|----------|------------|--------------|
| Hårdvara PC | TUXEDO | 🇩🇪 Tyskland |
| Hårdvara Mobil | Fairphone | 🇳🇱 Nederländerna |
| Mobil-OS | /e/OS | 🇫🇷 Frankrike |
| Produktivitetssvit | OpenDesk/Nextcloud | 🇩🇪 Tyskland (self-hosted) |
| E-post | Mailbox.org | 🇩🇪 Tyskland |
| VPN | Mullvad | 🇸🇪 Sverige |
| Lösenord | Vaultwarden | Self-hosted |
| Video | Jitsi Meet | Self-hosted |

#### Infomaniak 🇨🇭
- Schweiziskt, familjeägt sedan 1994
- kSuite: kDrive, kMail, kMeet, kChat
- Managed (ingen self-hosting)
- Datacenter i Schweiz
- Etiskt fokus, 100% förnybar energi

#### Nextcloud 🇩🇪
- Tyskt företag (Stuttgart)
- Self-hosted eller managed
- Files, Calendar, Mail, Talk, Office (Collabora)
- Stort app-ekosystem
- GDPR by design

#### OpenDesk 🇩🇪
- Tyskt regeringsinitiativ (ZenDiS)
- Self-hosted produktivitetssvit
- Inkluderar: Nextcloud Files, Collabora Office, Calendar, Talk
- Designat för offentlig sektor
- GDPR by design
