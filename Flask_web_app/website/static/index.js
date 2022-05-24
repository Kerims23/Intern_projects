function deleteNote(noteId){
    //take note id 
    fetch('/delete-note',{
        //send post request to delete-note 
        method: 'POST',
        body: JSON.stringify({ noteId: noteId })
    }).then((_res) =>{
        window.location.href = "/";
        //after response it will reload the window to home page, refresh
    });
}