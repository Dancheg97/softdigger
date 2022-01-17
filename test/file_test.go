package main

import "testing"

func TestSum(t *testing.T) {
	if a := sum(1, 10); a != 11 {
		t.Error("sum incorrect")
	}
	if a := sum(2, 7); a != 9 {
		t.Error("sum incorrect")
	}
}
