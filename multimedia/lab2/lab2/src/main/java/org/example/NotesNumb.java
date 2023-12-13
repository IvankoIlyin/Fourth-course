package org.example;

public enum NotesNumb {
    C(0),
    C_DIEZ(1),
    D(2),
    D_DIEZ(3),
    E(4),
    F(5),
    F_DIEZ(6),
    G(7),
    G_DIEZ(8),
    A(9),
    A_DIEZ(10),
    B(11);


    private int num;
    NotesNumb(int _num) {
        this.num=_num;
    }

    public int getNum() {
        return num;
    }
}
