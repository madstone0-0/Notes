basedir="/mnt/windows/Users/HP/Documents/Notes/"

updateLog="update.log"

log() {
	touch $updateLog
	echo "$(date): $1" | tee -a "$basedir/$updateLog"
}

link_template() {
	ln -s "$basedir/Templates/latex_template" "template"
}

update_links() {
	for file in $(fd --hidden -g "template" .); do
		log "Saw $file"
		log "Removing $file"
		rm -rf "$file"
		log "Linking to $file"
		ln -s "$basedir/Templates/latex_template" "$file"
	done
}
