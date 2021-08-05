package reto3;
public class Paciente extends Persona{
    
    private String naucea, vomito, dolorAbdominal, diarrea, fiebre;

    public Paciente() {
    }

    public Paciente(String nombre, String cedula, String naucea, String vomito, 
            String dolorAbdominal, String diarrea, String fiebre) {
        super(nombre, cedula);
        this.naucea = naucea;
        this.vomito = vomito;
        this.dolorAbdominal = dolorAbdominal;
        this.diarrea = diarrea;
        this.fiebre = fiebre;
    }

    
    public String diagnosticar(String naucea, String vomito, String dolorAbdominal,
    String diarrea, String fiebre){        
        String diagnostico = "";
        if(naucea.equalsIgnoreCase("si") && vomito.equalsIgnoreCase("si")
                    && dolorAbdominal.equalsIgnoreCase("si")
                    && diarrea.equalsIgnoreCase("si")
                    && fiebre.equalsIgnoreCase("si")){
                diagnostico = "Staphylococcus aureus";
            }else if(naucea.equalsIgnoreCase("si") && vomito.equalsIgnoreCase("si")
                    && dolorAbdominal.equalsIgnoreCase("no")
                    && diarrea.equalsIgnoreCase("no")
                    && fiebre.equalsIgnoreCase("no")){
                diagnostico = "Bacillus cereus";
            }else if(naucea.equalsIgnoreCase("no") && vomito.equalsIgnoreCase("no")
                    && dolorAbdominal.equalsIgnoreCase("si")
                    && diarrea.equalsIgnoreCase("no")
                    && fiebre.equalsIgnoreCase("si")){
                diagnostico = "Taenia saginata";
            }else if(naucea.equalsIgnoreCase("si") && vomito.equalsIgnoreCase("si")
                    && dolorAbdominal.equalsIgnoreCase("no")
                    && diarrea.equalsIgnoreCase("si")
                    && fiebre.equalsIgnoreCase("si")){
                diagnostico = "Norovirus";
            }else if(naucea.equalsIgnoreCase("no") && vomito.equalsIgnoreCase("si")
                    && dolorAbdominal.equalsIgnoreCase("no")
                    && diarrea.equalsIgnoreCase("si")
                    && fiebre.equalsIgnoreCase("no")){
                diagnostico = "Rotavirus";
            }else{
                diagnostico = "Sin diagnostico";
            }            
        return diagnostico;
    }

    public void setVomito(String vomito) {
        this.vomito = vomito;
    }

    public void setDolorAbdominal(String dolorAbdominal) {
        this.dolorAbdominal = dolorAbdominal;
    }

    public void setDiarrea(String diarrea) {
        this.diarrea = diarrea;
    }

    public void setFiebre(String fiebre) {
        this.fiebre = fiebre;
    }   
    
    public String getNaucea() {
        return naucea;
    }

    public String getVomito() {
        return vomito;
    }

    public String getDolorAbdominal() {
        return dolorAbdominal;
    }
    
    public String getDiarrea() {
        return diarrea;
    }

    public String getFiebre() {
        return fiebre;
    }
    
}
