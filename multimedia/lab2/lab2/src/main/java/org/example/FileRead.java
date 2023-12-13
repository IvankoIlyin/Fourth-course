package org.example;


import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class FileRead {
    private String path;
    private String text_file="";


    public FileRead(String _path) {
        this.path=_path;
    }

    private void read_file(){
        try (BufferedReader reader = new BufferedReader(new FileReader(this.path))) {
            String line;
            while ((line = reader.readLine()) != null) {
                this.text_file+=line+ "\n";
            }
        }
        catch (IOException e) {
            e.printStackTrace();
        }
    }

    public String[] get_notes_list(){
        this.read_file();
        String[] notes = this.text_file.split("\\s+");
        return notes;
    }


}
