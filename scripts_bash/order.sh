#!/bin/bash
# Script para organizar archivos por extensión

declare -a extenciones=()

for i in *; do
    # Verificar que es un archivo y no un directorio
    if [[ -f "$i" ]]; then
        ext="${i##*.}"
        
        # Evitar procesar archivos sin extensión
        if [[ "$ext" == "$i" ]]; then
            continue
        fi

        # Crear la carpeta si no existe
        if ! printf "%s\n" "${extenciones[@]}" | grep -qx "$ext"; then
            extenciones+=("$ext")
            mkdir -p "$ext"  # -p evita error si la carpeta ya existe
        fi

        # Mover el archivo a su respectiva carpeta
        mv "$i" "./$ext/"
    fi
done

# Mostrar las extensiones procesadas
echo "Archivos organizados en las carpetas: ${extenciones[@]}"



