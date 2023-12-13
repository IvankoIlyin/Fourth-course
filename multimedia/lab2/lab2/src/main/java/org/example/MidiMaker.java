package org.example;

import jm.JMC;
import jm.music.data.*;
import jm.util.*;


public class MidiMaker {
   private Score score;
   private Part part;
   private String[] notes;
    private double BPM;

    MidiMaker(String path,double _BPM,double _time_signature){
        score = new Score("Generated MIDI");
        part = new Part("Piano",JMC.PIANO);
        FileRead fr = new FileRead(path);
        this.notes=fr.get_notes_list();
        this.BPM=_BPM;
    }

    public void generate_midi(){

       for(String curr_chord:this.notes){
           String[] note_list=curr_chord.split(",");
           Phrase phrase =new Phrase();
           for(int i=2;i<note_list.length;i++){
               int octave_num=Integer.parseInt(String.valueOf(note_list[0]));
               int note_duration = Integer.parseInt(String.valueOf(note_list[1]));
               int note_num=NotesNumb.valueOf(note_list[i]).getNum();
               int midi_code=(octave_num*12)+note_num;
               double duration = 60/this.BPM * 4/note_duration;
               phrase.addNote(new Note(midi_code, duration));
           }
           this.part.addPhrase(phrase);

       }
        this.score.addPart(part);
        Write.midi(score, "generated_composition.mid");

    }

    public void play_midi(){
        this.generate_midi();
        Play.midi(this.score);
    }


}
