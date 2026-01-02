#!/usr/bin/env bash
# Script for DNS enumeration if domain name and IP address is known
# Usage check
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <DNS_SERVER_IP> <DOMAIN>"
    exit 1
fi

DNS_SERVER="$1"
DOMAIN="$2"
OUTPUT_FILE="dns_report.txt"

# Common and useful DNS record types for recon / CTFs
RECORD_TYPES=(
    A
    AAAA
    NS
    MX
    SOA
    TXT
    CNAME
    PTR
    SRV
    SPF
    CAA
    DNSKEY
    DS
    RRSIG
    NSEC
    ANY
)

# Start report
echo "DNS Enumeration Report" > "$OUTPUT_FILE"
echo "Server: $DNS_SERVER" >> "$OUTPUT_FILE"
echo "Domain: $DOMAIN" >> "$OUTPUT_FILE"
echo "Generated: $(date)" >> "$OUTPUT_FILE"
echo "==========================================" >> "$OUTPUT_FILE"
echo >> "$OUTPUT_FILE"

# Run dig for each record type
for TYPE in "${RECORD_TYPES[@]}"; do
    echo "### Record Type: $TYPE ###" >> "$OUTPUT_FILE"
    dig @"$DNS_SERVER" "$DOMAIN" "$TYPE" \
        +noall +answer +authority +additional >> "$OUTPUT_FILE"
    echo >> "$OUTPUT_FILE"
done

# Zone transfer attempt (important in CTFs)
echo "### Zone Transfer Attempt (AXFR) ###" >> "$OUTPUT_FILE"
dig @"$DNS_SERVER" "$DOMAIN" AXFR >> "$OUTPUT_FILE"
echo >> "$OUTPUT_FILE"

echo "[+] DNS enumeration complete. Results saved to $OUTPUT_FILE"
