#!/bin/bash

# ================================
#   SCRIPT DE MONITORIZAÇÃO
# ================================

mkdir -p relatorios

opcoes=("Informações do Sistema" "Analisar Logs" "Top Processos" "Sair")

gerar_relatorio() {
    DATA=$(date +"%Y%m%d_%H%M%S")
    FICHEIRO="relatorios/relatorio_$DATA.txt"

    echo "===== RELATÓRIO DO SISTEMA =====" > $FICHEIRO
    echo "Data: $(date)" >> $FICHEIRO
    echo "Utilizador: $USER" >> $FICHEIRO
    echo "Hostname: $(hostname)" >> $FICHEIRO
    echo "" >> $FICHEIRO

    echo "===== MEMÓRIA =====" >> $FICHEIRO
    free -h >> $FICHEIRO
    echo "" >> $FICHEIRO

    echo "===== DISCO =====" >> $FICHEIRO
    df -h >> $FICHEIRO
    echo "" >> $FICHEIRO

    echo "===== IP PÚBLICO =====" >> $FICHEIRO
    curl -s ifconfig.me >> $FICHEIRO
    echo "" >> $FICHEIRO

    echo "===== PROCESSOS MAIS PESADOS =====" >> $FICHEIRO
    ps aux --sort=-%cpu | head -10 >> $FICHEIRO

    echo "Relatório criado em: $FICHEIRO"
}

analisar_logs() {
    LOG="/var/log/syslog"

    if [[ ! -f "$LOG" ]]; then
        echo "O ficheiro de log não existe."
        return
    fi

    echo "Últimas 20 linhas do syslog:"
    tail -20 "$LOG"
}

top_processos() {
    echo "Top 10 processos por CPU:"
    ps aux --sort=-%cpu | head -10
}

while true; do
    echo ""
    echo "===== MENU ====="

    for i in "${!opcoes[@]}"; do
        echo "$((i+1))) ${opcoes[$i]}"
    done

    read -p "Escolha uma opção: " escolha

    case $escolha in
        1) gerar_relatorio ;;
        2) analisar_logs ;;
        3) top_processos ;;
        4) echo "A sair..."; exit 0 ;;
        *) echo "Opção inválida!" ;;
    esac
done
