package org.example;

import jm.music.data.Note;
import jm.music.data.Part;
import jm.music.data.Phrase;
import jm.music.data.Score;
import jm.util.Play;
import jm.*;

public class Main {
    public static void main(String[] args) {

        MidiMaker md = new MidiMaker("src/main/java/resources/file_2.txt",220,1);
        md.play_midi();
    }

    }
