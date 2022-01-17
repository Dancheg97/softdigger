package main

import (
	"encoding/json"
	"io/ioutil"
	"net/http"
)

type mes struct {
	Message string `json:"message"`
}

var lastMes = "no message"

func homePage(w http.ResponseWriter, r *http.Request) {
	json.NewEncoder(w).Encode(lastMes)
	reqBody, _ := ioutil.ReadAll(r.Body)
	var ms mes
	json.Unmarshal(reqBody, &ms)
	lastMes = ms.Message
}

func main() {
	http.HandleFunc("/", homePage)
	http.ListenAndServe(":10000", nil)
}
