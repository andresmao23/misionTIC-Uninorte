/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package reto3;

import java.net.URL;
import java.util.ResourceBundle;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.RadioButton;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;
import javafx.scene.control.ToggleGroup;

/**
 *
 * @author andre
 */
public class FXMLDocumentController implements Initializable {

    @FXML
    private TextField txtNombre;
    
    @FXML
    private TextField txtCedula;
    private TextField txtDiarrea;
    
    
    @FXML
    private TextArea taDatosIngresados, taSalidas;
    @FXML
    private Button btnIngresar;
    @FXML
    private Button btnProcesar;
    @FXML
    private RadioButton rbMasculino;
    @FXML
    private RadioButton rbFemenino;
    @FXML
    private ToggleGroup tgGenero;
    @FXML
    private RadioButton rbNauceasSi;
    @FXML
    private ToggleGroup tgNauceas;
    @FXML
    private RadioButton rbNauceasNo;
    @FXML
    private RadioButton rbVomitoSi;
    @FXML
    private ToggleGroup tgVomito;
    @FXML
    private RadioButton rbVomitoNo;
    @FXML
    private RadioButton rbDolorSi;
    @FXML
    private ToggleGroup tgDolor;
    @FXML
    private RadioButton rbDolorNo;
    @FXML
    private RadioButton rbDiarreaSi;
    @FXML
    private RadioButton rbDiarreaNo;
    @FXML
    private ToggleGroup tgDiarrea;
    @FXML
    private RadioButton rbFiebreSi;
    @FXML
    private ToggleGroup tgFiebre;
    @FXML
    private RadioButton rbFiebreNo;
    
    /*@FXML
    private void handleButtonAction(ActionEvent event) {
        System.out.println("You clicked me!");
    }*/
    @FXML
    private void ingresar(ActionEvent event) {
        String genero = "";
        if(rbMasculino.isSelected()== true)
            genero = "M";
        else if(rbFemenino.isSelected()==true)
            genero = "F";
        
        String naucea = "";
        if(rbNauceasSi.isSelected()== true)
            naucea = "si";
        else if(rbNauceasNo.isSelected()==true)
            naucea = "no";
        
        String vomito = "";
        if(rbVomitoSi.isSelected()== true)
            vomito = "si";
        else if(rbVomitoNo.isSelected()==true)
            vomito = "no";
        
        String dolor = "";
        if(rbDolorSi.isSelected()== true)
            dolor = "si";
        else if(rbDolorNo.isSelected()==true)
            dolor = "no";
        
        String diarrea = "";
        if(rbDiarreaSi.isSelected()== true)
            diarrea = "si";
        else if(rbDiarreaNo.isSelected()==true)
            diarrea = "no";
        
        String fiebre = "";
        if(rbFiebreSi.isSelected()== true)
            fiebre = "si";
        else if(rbFiebreNo.isSelected()==true)
            fiebre = "no";
            
        taDatosIngresados.appendText(txtNombre.getText()+" "+txtCedula.getText()+" "+
                genero +" "+naucea+" "+vomito+" "+dolor+" "+diarrea+" "+fiebre+"\n");
    }
    
    @FXML
    private void procesar(ActionEvent event){
        taSalidas.setText("");
        //System.out.println(taDatosIngresados.getText());
        System.out.println(contarLineasTextArea(taDatosIngresados.getText()));
        
        String [] diagnosticos = {
            "Staphylococcus aureus",
            "Bacillus cereus",
            "Taenia saginata",
            "Norovirus",
            "Rotavirus",
            "Sin diagnostico"
        };
        
        int contDiagnostico1 = 0;
        int contDiagnostico2 = 0;
        int contDiagnostico3 = 0;
        int contDiagnostico4 = 0;
        int contDiagnostico5 = 0;
        int contDiagnostico6 = 0;
        
        int lineas = contarLineasTextArea(taDatosIngresados.getText());
        
        String [] datosPacientes = taDatosIngresados.getText().split("\n");
        //String[] palabra = taDatosIngresados.getText().split("\n");
        /*for (int i = 0; i < palabra.length; i++) {
            System.out.println(palabra[i]);
        }*/
        /*for (int i = 0; i < datosPacientes.length; i++) {
            datosPacientes[i] = palabra.split(" ");
        }*/
        
        for(int i=0;i<datosPacientes.length;i++){
            /*String nombre = datosPacientes[i].split(" ")[0];
            String cedula = datosPacientes[i].split(" ")[1];
            String naucea = datosPacientes[i].split(" ")[2];
            String vomito = datosPacientes[i].split(" ")[3];
            String dolorAbdominal = datosPacientes[i].split("-")[4];
            String diarrea = datosPacientes[i].split(" ")[5];
            String fiebre = datosPacientes[i].split(" ")[6];*/
            String [] linea = datosPacientes[i].split(" ");
            String nombre = linea[0] + linea[1];
            String cedula = linea[2];
            String genero = linea[3];
            String naucea = linea[4];
            String vomito = linea[5];
            String dolorAbdominal = linea[6];
            String diarrea = linea[7];
            String fiebre = linea[8];
            Paciente paciente = new Paciente(nombre, cedula, naucea, vomito, 
                    dolorAbdominal, diarrea, fiebre);
            
            String diagnostico = paciente.diagnosticar(naucea, vomito, 
                    dolorAbdominal, diarrea, fiebre);
            
            if(diagnostico.equalsIgnoreCase("Staphylococcus aureus")){
                //System.out.println(paciente.getCedula() + " " + diagnostico);
                taSalidas.appendText(paciente.getCedula()+" "+ diagnostico+"\n");
                contDiagnostico1+=1;
            }else if(diagnostico.equalsIgnoreCase("Bacillus cereus")){
                //System.out.println(paciente.getCedula() + " " + diagnostico);
                taSalidas.appendText(paciente.getCedula()+" "+ diagnostico+"\n");
                contDiagnostico2+=1;
            }else if(diagnostico.equalsIgnoreCase("Taenia saginata")){
                //System.out.println(paciente.getCedula() + " " + diagnostico);
                taSalidas.appendText(paciente.getCedula()+" "+ diagnostico+"\n");
                contDiagnostico3+=1;
            }else if(diagnostico.equalsIgnoreCase("Norovirus")){
                //System.out.println(paciente.getCedula() + " " + diagnostico);
                taSalidas.appendText(paciente.getCedula()+" "+ diagnostico+"\n");
                contDiagnostico4+=1;
            }else if(diagnostico.equalsIgnoreCase("Rotavirus")){
                //System.out.println(paciente.getCedula() + " " + diagnostico);
                taSalidas.appendText(paciente.getCedula()+" "+ diagnostico+"\n");
                contDiagnostico5+=1;
            }else if(diagnostico.equalsIgnoreCase("Sin diagnostico")){
                //System.out.println(paciente.getCedula() + " " + diagnostico);
                taSalidas.appendText(paciente.getCedula()+" "+ diagnostico+"\n");
                contDiagnostico6+=1;
            }            
        }
        
        if(contDiagnostico1>=contDiagnostico2 && contDiagnostico1>=contDiagnostico3
                && contDiagnostico1>=contDiagnostico4 && contDiagnostico1>=contDiagnostico5
                && contDiagnostico1>=contDiagnostico6){
                //System.out.println(diagnosticos[0]);
                taSalidas.appendText(diagnosticos[0]);
        }else if(contDiagnostico2>=contDiagnostico1 && contDiagnostico2>=contDiagnostico3
                && contDiagnostico2>=contDiagnostico4 && contDiagnostico2>=contDiagnostico5
                && contDiagnostico2>=contDiagnostico6){
                //System.out.println(diagnosticos[1]);
                taSalidas.appendText(diagnosticos[1]);
        }else if(contDiagnostico3>=contDiagnostico1 && contDiagnostico3>=contDiagnostico2
                && contDiagnostico3>=contDiagnostico4 && contDiagnostico3>=contDiagnostico5
                && contDiagnostico3>=contDiagnostico6){
                //System.out.println(diagnosticos[2]);
                taSalidas.appendText(diagnosticos[2]);
        }else if(contDiagnostico4>=contDiagnostico1 && contDiagnostico4>=contDiagnostico2
                && contDiagnostico4>=contDiagnostico3 && contDiagnostico4>=contDiagnostico5
                && contDiagnostico4>=contDiagnostico6){
                //System.out.println(diagnosticos[3]);
                taSalidas.appendText(diagnosticos[3]);
        }else if(contDiagnostico5>=contDiagnostico1 && contDiagnostico5>=contDiagnostico2
                && contDiagnostico5>=contDiagnostico3 && contDiagnostico5>=contDiagnostico4
                && contDiagnostico5>=contDiagnostico6){
                //System.out.println(diagnosticos[4]);
                taSalidas.appendText(diagnosticos[4]);
        }else if(contDiagnostico6>=contDiagnostico1 && contDiagnostico6>=contDiagnostico2
                && contDiagnostico6>=contDiagnostico3 && contDiagnostico6>=contDiagnostico4
                && contDiagnostico6>=contDiagnostico5){
                //System.out.println(diagnosticos[5]);
                taSalidas.appendText(diagnosticos[5]);
            }
        
        //System.out.println(contDiagnostico6);
        taSalidas.appendText("\n" + contDiagnostico6+"");
    }
    
    @Override
    public void initialize(URL url, ResourceBundle rb) {
        // TODO
    }    
    
    public int contarLineasTextArea(String texto) {
        int lineas = 0;
        for (int j = 0; j < texto.length(); j++) {
            if (texto.charAt(j)=='\n'){
                lineas++;
            }
        }
        return lineas;
    }
    
}
