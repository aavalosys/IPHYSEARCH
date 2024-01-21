<template>

    <main class="main">
            <!-- Breadcrumb -->
            <ol class="breadcrumb">
                <li class="breadcrumb-item">Inicio</li>
                <li class="breadcrumb-item"><a href="#">Membresía</a></li>
                <li class="breadcrumb-item active">Miembros</li>
            </ol>
            <div class="container-fluid">
                <!-- Ejemplo de tabla Listado -->
                <div class="card">
                    <div class="card-header">
                        <i class="fa fa-align-justify"></i> Miembros
                        <button type="button" @click="abrirmodal('miembro','registrar','')" class="btn btn-secondary">
                            <i class="icon-plus"></i>&nbsp;Nuevo
                        </button>
                    </div>
                    <div class="card-body">
                        <div class="form-group row">
                            <div class="col-md-6">
                                <div class="input-group">
                                    <select class="form-control col-md-3" v-model="criterio">
                                      <option value="nombre">Nombre</option>
                                      <option value="dpi">CUI</option>
                                    </select>
                                    <input type="text" v-model="buscar" @keyup.enter="listarMiembro(1, buscar, criterio)" class="form-control" placeholder="Texto a buscar">
                                    <button type="submit" @click="listarMiembro(1, buscar, criterio)" class="btn btn-primary"><i class="fa fa-search"></i> Buscar</button>
                                </div>
                            </div>
                        </div>
                        <table class="table table-bordered table-striped table-sm">
                            <thead>
                                <tr>
                                    <th>Opciones</th>
                                    <th>No. Registro</th>
                                    <th>Folio</th>
                                    <th>Nombre</th>
                                    <th>DPI</th>
                                    <th>Estado</th>
                                    <th>Foto</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr v-for="miembro in arrayMiembro" :key="miembro.idmiembro">
                                    <td>
                                        <button @click="abrirmodal('miembro','actualizar', miembro)" type="button" class="btn btn-warning btn-sm">
                                          <i class="icon-pencil"></i>
                                        </button> &nbsp;
                                        <template v-if="miembro.estado">
                                            <button type="button" class="btn btn-danger btn-sm" @click="desactivarMiembro(miembro.idmiembro)">
                                                <i class="icon-trash"></i>
                                            </button>
                                        </template>
                                        <template v-else>
                                            <button type="button" class="btn btn-success btn-sm" @click="activarMiembro(miembro.idmiembro)">
                                                <i class="icon-check"></i>
                                            </button>
                                        </template>
                                    </td>
                                    <td v-text="miembro.registro"></td>
                                    <td v-text="miembro.folio"></td>
                                    <td v-text="miembro.nombre"></td>
                                    <td v-text="miembro.dpi"></td>
                                    <td>
                                        <div v-if="miembro.estado">
                                            <span class="badge badge-success">Activo</span>             
                                        </div>
                                        <div v-else>
                                            <span class="badge badge-danger">Inactivo</span>             
                                        </div>
                                    </td>
                                    <td>
                                        <div>
                                            <button @click="abrirmodal2(miembro)" type="button" class="btn btn-success btn-sm">
                                                <i class="icon-sheet">Ver</i>
                                            </button> &nbsp;            
                                        </div>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                        <nav>
                            <ul class="pagination">
                                <li class="page-item" v-if="pagination.current_page >1">
                                    <a class="page-link" @click.prevent="cambiarPagina(pagination.currentPage -  1,buscar,criterio)" href="#">Ant</a>
                                </li>
                                <li class="page-item" v-for="page in pagesNumber" :key="page" :class="[page == isActived ? 'active' : '']">
                                    <a class="page-link" @click.prevent="cambiarPagina(page,buscar,criterio)"  v-text="page" href="#" ></a>
                                </li>
                                <li class="page-item" v-if="pagination.current_page < pagination.last_page">
                                    <a class="page-link" @click.prevent="cambiarPagina(pagination.currentPage +  1,buscar,criterio)" href="#" > Sig</a>
                                </li>
                            </ul>
                        </nav>
                    </div>
                </div>
                <!-- Fin ejemplo de tabla Listado -->
            </div>
            <!--Inicio del modal agregar/actualizar-->
            <div class="modal fade" tabindex="-1" :class="{'mostrar' : modal}" role="dialog" aria-labelledby="myModalLabel" style="display: none;" aria-hidden="true">
                <div class="modal-dialog modal-primary modal-lg" role="document">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h4 class="modal-title" v-text="tituloModal"></h4>
                            <button type="button" class="close" @click="cerrarmodal()" aria-label="Close">
                              <span aria-hidden="true">×</span>
                            </button>
                        </div>
                        <div class="modal-body">
                            
                                <div class="form-group row">
                                    
                                    <label class="col-md-3 form-control-label" for="text-input">Nombre</label>
                                    <div class="col-md-9">
                                        <input type="text" v-model="nombre" class="form-control" placeholder="Nombre de Persona">
                                    </div>
                                </div>
                                <div class="form-group row">
                                    <label class="col-md-3 form-control-label" for="text-input">DPI</label>
                                    <div class="col-md-9">
                                        <input type="text" v-model="cui" class="form-control" placeholder="DPI">
                                    </div>
                                </div>
                                <div class="form-group row">
                                    <label class="col-md-3 form-control-label" for="text-input">Genero</label>
                                    <div class="col-md-9">
                                        <select class="form-control" v-model="idgenero">
                                            <option value="0">--- Seleccione ---</option>
                                            <option v-for="genero in arrayGenero" :key="genero.idgenero" :value="genero.idgenero" :select="genero.idgenero == idgenero" v-text="genero.descripcion"></option>
                                        </select>
                                    </div>
                                </div>
                                <div class="form-group row">
                                    <label class="col-md-3 form-control-label" for="text-input">Estado Civil</label>
                                    <div class="col-md-9">
                                        <select class="form-control" v-model="idestadocivil">
                                            <option value="0">--- Seleccione ---</option>
                                            <option v-for="estadocivil in arrayEstadoCivil" :key="estadocivil.idestadocivil" :value="estadocivil.idestadocivil"  :select="estadocivil.idestadocivil == idestadocivil" v-text="estadocivil.descripcion"></option>
                                        </select>
                                    </div>
                                </div>
                                <div class="form-group row">
                                    <label class="col-md-3 form-control-label" for="text-input">Fecha de Nacimiento</label>
                                    <div class="col-md-9">
                                        <input type="text" v-model="fechanacimiento"  class="form-control" placeholder="">
                                    </div>
                                </div>
                                <div class="form-group row">
                                    <label class="col-md-3 form-control-label" for="text-input">Lugar de Nacimiento</label>
                                    <div class="col-md-9">
                                        <input type="text" v-model="lugarnacimiento" class="form-control" placeholder="">
                                    </div>
                                </div>
                                <div class="form-group row">
                                    <label class="col-md-3 form-control-label" for="text-input">Departamento</label>
                                    <div class="col-md-9">
                                        <select class="form-control" v-model="iddepartamento" @change="selectMunicipio(iddepartamento)">
                                        <option value="0">--- Seleccione ---</option>
                                        <option v-for="departamento in arrayDepartamento" :key="departamento.iddepartamento" :value="departamento.iddepartamento" :select="departamento.iddepartamento == iddepartamento" v-text="departamento.descripcion"></option>
                                        </select>
                                    </div>
                                </div>
                                <div class="form-group row">
                                    <label class="col-md-3 form-control-label" for="text-input">Municipio</label>
                                    <div class="col-md-9" >
                                        <select class="form-control" v-model="idmunicipio" >
                                        <option value="0">--- Seleccione ---</option>
                                        <option v-for="municipio in arrayMunicipio" :key="municipio.idmunicipio" :value="municipio.idmunicipio" v-text="municipio.descripcion"></option>
                                        </select>
                                    </div>
                                </div>
                                <div class="form-group row">
                                    <label class="col-md-3 form-control-label" for="text-input">Profesión</label>
                                    <div class="col-md-9">
                                        <input type="text" v-model="profesion"  class="form-control" placeholder="">
                                    </div>
                                </div>
                                <div class="form-group row">
                                    <label class="col-md-3 form-control-label" for="text-input">Oficio</label>
                                    <div class="col-md-9">
                                        <input type="text" v-model="oficio"  class="form-control" placeholder="">
                                    </div>
                                </div>
                                <div class="form-group row">
                                    <label class="col-md-3 form-control-label" for="text-input">Fecha de Conversión</label>
                                    <div class="col-md-9">
                                        <input type="text" v-model="fechaconversion"  class="form-control" placeholder="">
                                    </div>
                                </div>
                                <div class="form-group row">
                                    <label class="col-md-3 form-control-label" for="text-input">Lugar de Conversión</label>
                                    <div class="col-md-9">
                                        <input type="text" v-model="lugarconversion"  class="form-control" placeholder="">
                                    </div>
                                </div>
                                <div class="form-group row">
                                    <label class="col-md-3 form-control-label" for="text-input">Fecha de Bautismo en Aguas</label>
                                    <div class="col-md-9">
                                        <input type="text" v-model="fechabautismoa"  class="form-control" placeholder="">
                                    </div>
                                </div>
                                <div class="form-group row">
                                    <label class="col-md-3 form-control-label" for="text-input">Lugar de Bautismo en Aguas</label>
                                    <div class="col-md-9">
                                        <input type="text" v-model="lugarbautismoa"  class="form-control" placeholder="">
                                    </div>
                                </div>
                                <div class="form-group row">
                                    <label class="col-md-3 form-control-label" for="text-input">Fecha de Recepción</label>
                                    <div class="col-md-9">
                                        <input type="text" v-model="fecharecepcion"  class="form-control" placeholder="">
                                    </div>
                                </div>
                                <div class="form-group row">
                                    <label class="col-md-3 form-control-label" for="text-input">Lugar de Recepción</label>
                                    <div class="col-md-9">
                                        <input type="text" v-model="lugarrecepcion"  class="form-control" placeholder="">
                                    </div>
                                </div>
                                <div class="form-group row">
                                    <label class="col-md-3 form-control-label" for="text-input">Fecha de Bautismo con Espíritu Santo</label>
                                    <div class="col-md-9">
                                        <input type="text" v-model="fechabautismoe"  class="form-control" placeholder="">
                                    </div>
                                </div>
                                <div class="form-group row">
                                    <label class="col-md-3 form-control-label" for="text-input">Lugar de Bautismo con Espíritu Santo</label>
                                    <div class="col-md-9">
                                        <input type="text" v-model="lugarbautismoe"  class="form-control" placeholder="">
                                    </div>
                                </div>
                                <div class="form-group row">
                                    <label class="col-md-3 form-control-label" for="text-input">Fecha de Pacto</label>
                                    <div class="col-md-9">
                                        <input type="text" v-model="fechapacto"  class="form-control" placeholder="">
                                    </div>
                                </div>
                                <div class="form-group row">
                                    <label class="col-md-3 form-control-label" for="text-input">Traslado a:</label>
                                    <div class="col-md-9">
                                        <input type="text" v-model="traslado"  class="form-control" placeholder="">
                                    </div>
                                </div>
                                <div class="form-group row">
                                    <label class="col-md-3 form-control-label" for="text-input">Foto</label>
                                    <div class="col-md-9" >
                                        <input type="file" @change="obtenerImagen">
                                    </div>
                                </div>
                                <div v-show="errorMiembro" class="form-group row alert alert-danger">
                                    <div v-for="error in mostrarError" :key="error" v-text="error + '\n'" class="">
                                        
                                    </div>
                                </div>
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-secondary" @click="cerrarmodal()">Cerrar</button>
                            <button type="button" v-if="tipoAccion==1"  class="btn btn-primary" @click="insertarMiembro()">Guardar</button>
                            <button type="button" v-if="tipoAccion==2" class="btn btn-primary" @click="actualizarMiembro()">Actualizar</button>
                        </div>
                    </div>
                    <!-- /.modal-content -->
                </div>
                <!-- /.modal-dialog -->
            </div>
            <!--Fin del modal-->
            <!--Inicio del modal agregar/actualizar-->
            <div class="modal fade" tabindex="-1" :class="{'mostrar2' : modal2}" role="dialog" aria-labelledby="myModalLabel" style="display: none;" aria-hidden="true">
                <div class="modal-dialog modal-primary modal-lg" role="document">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h4 class="modal-title" v-text="tituloModal2"></h4>
                            <button type="button" class="close" @click="cerrarmodal2()" aria-label="Close">
                              <span aria-hidden="true">×</span>
                            </button>
                        </div>
                        <div class="modal-body"> 
                           <p class=""><img class="img-fluid" :src="'../storage/fotos/'+foto" /></p>
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-secondary" @click="cerrarmodal2()">Cerrar</button>
                        </div>
                    </div>
                    <!-- /.modal-content -->
                </div>
                <!-- /.modal-dialog -->
            </div>
            <!--Fin del modal-->

    </main>
</template>

<script>
    
    import moment from'moment';

    export default {
        data(){
            return {
                idmiembro : 0,
                nombre : '',
                cui : '',
                fechanacimiento : '',
                lugarnacimiento : '',
                fechaconversion : '',
                lugarconversion : '',
                fechabautismoa : '',
                lugarbautismoa : '',
                fecharecepcion : '',
                lugarrecepcion : '',
                fechabautismoe : '',
                lugarbautismoe : '',
                fechapacto : '',
                foto: '',
                imagen: '',
                idmunicipio : '',
                idgenero: '',
                idestadocivil: '',
                profesion: '',
                oficio: '',
                folio : '',
                iddepartamento : '',
                arrayMiembro : [],
                arrayGenero: [],
                arrayEstadoCivil: [],
                arrayDepartamento : [],
                arrayMunicipio : [],
                modal : 0,
                tituloModal : '',
                modal2 : 0,
                tituloModal2 : '',
                tipoAccion : 0,
                traslado : '',
                errorMiembro : 0,
                mostrarError : [],
                pagination : {
                    'total' : 0,
                    'per_page' : 0,
                    'current_page': 0,
                    'last_page': 0,
                    'from': 0,
                    'to': 0,
                },
                offset: 3,
                criterio : 'nombre',
                buscar : '',
                direccionFoto: ''

            }
        },
        computed: {
            isActived: function(){
                return this.pagination.current_page;
            },
            pagesNumber: function(){
                if(!this.pagination.to){
                    return [];
                }

                var from = this.pagination.current_page - this.offset;
                if(from < 1){
                    from = 1;
                }

                var to = from + (this.offset * 2);
                if (to >= this.pagination.last_page){
                    to = this.pagination.last_page;
                }

                var pagesArray = [];
                while(from <= to){
                    pagesArray.push(from);
                    from++;
                }
                return pagesArray;
            }
        },
        methods : {
            obtenerImagen(event){
                this.imagen = event.target.files[0];
            },
            listarMiembro(page, buscar, criterio){
                let me = this;
                var url = '/miembros?page=' + page + '&buscar=' + buscar + '&criterio='+ criterio;
                axios.get(url).then(function (response){
                    var respuesta = response.data;
                    //console.log(response.data);
                    me.arrayMiembro = response.data.miembro.data;
                    me.pagination = respuesta.pagination;     
                })
                .catch(function (error){
                    console.log(error);
                });    
            },
            insertarMiembro(){
                if(this.validarMiembro()){
                    return;
                }

                let me = this;
                let formData = new FormData();
                formData.append('nombre', this.nombre);
                formData.append('imagen', this.imagen);
                formData.append('cui', this.cui);
                formData.append('fechanacimiento', this.fechanacimiento);
                formData.append('lugarnacimiento', this.lugarnacimiento);
                formData.append('fechaconversion', this.fechaconversion);
                formData.append('lugarconversion', this.lugarconversion);
                formData.append('fechabautismoa', this.fechabautismoa);
                formData.append('lugarbautismoa', this.lugarbautismoa);
                formData.append('fecharecepcion', this.fecharecepcion);
                formData.append('lugarrecepcion', this.lugarrecepcion);
                formData.append('fechabautismoe', this.fechabautismoe);
                formData.append('lugarbautismoe', this.lugarbautismoe);
                formData.append('fechapacto', this.fechapacto);
                formData.append('idmunicipio', this.idmunicipio);
                formData.append('idgenero', this.idgenero);
                formData.append('idestadocivil', this.idestadocivil);
                formData.append('foto', this.foto);
                formData.append('idmunicipio', this.idmunicipio);
                formData.append('profesion', this.profesion);
                formData.append('oficio', this.oficio);
                formData.append('traslado', this.traslado);
                axios.post('miembros/registrar', formData, {    
                    headers: {
                            'Content-Type': 'multipart/form-data'
                        }
               })
                .then(response =>{
                    //console.log(response);
                    me.cerrarmodal();
                    me.listarMiembro(1, '', 'nombre');
                
                })
                .catch(error =>{
                    // handle error
                    if(error.response){
                        var obj = error.response.data.errors;
                        var objeto2 = Object.values(obj);
                        var mensajes = Object.values(objeto2);
                        
                        for (var x=0;x<mensajes.length;x++) {
                            for (var y=0;y<mensajes[x].length;y++) {
                                this.mostrarError.push(mensajes[x][y]); 
                            }
                        }

                        this.errorMiembro = 1;
                        return this.errorMiembro;

                    }
                    //console.log(error.response);
                });   
            
            },
            actualizarMiembro(){  
                if(this.validarMiembro()){
                    return;
                }
                let me = this;
                let formData = new FormData();
                formData.append('_method', 'PUT');
                formData.append('nombre', this.nombre);
                formData.append('imagen', this.imagen);
                formData.append('cui', this.cui);
                formData.append('fechanacimiento', this.fechanacimiento); 
                formData.append('lugarnacimiento', this.lugarnacimiento);
                formData.append('fechaconversion', this.fechaconversion);
                formData.append('lugarconversion', this.lugarconversion);
                formData.append('fechabautismoa', this.fechabautismoa);
                formData.append('lugarbautismoa', this.lugarbautismoa);
                formData.append('fecharecepcion', this.fecharecepcion);
                formData.append('lugarrecepcion', this.lugarrecepcion);
                formData.append('fechabautismoe', this.fechabautismoe);
                formData.append('lugarbautismoe', this.lugarbautismoe);
                formData.append('fechapacto', this.fechapacto);
                formData.append('idmunicipio', this.idmunicipio);
                formData.append('idgenero', this.idgenero);
                formData.append('idestadocivil', this.idestadocivil);
                formData.append('foto', this.foto);
                formData.append('idmunicipio', this.idmunicipio);
                formData.append('id', this.idmiembro);
                formData.append('profesion', this.profesion);
                formData.append('oficio', this.oficio);
                formData.append('traslado', this.traslado);
                axios.post('miembros/actualizar', formData)
                .then(response =>{
                    //console.log(response);
                    me.cerrarmodal();
                    me.listarMiembro(1, '', 'nombre');             
                })
                .catch(error =>{
                    // handle error
                    if(error.response){
                        var obj = error.response.data.errors;
                        var objeto2 = Object.values(obj);
                        var mensajes = Object.values(objeto2);
                        for (var x=0;x<mensajes.length;x++) {
                            for (var y=0;y<mensajes[x].length;y++) {
                                this.mostrarError.push(mensajes[x][y]); 
                            }
                        }
                        this.errorMiembro = 1;
                        return this.errorMiembro;
                    }
                });   
            },
            activarMiembro(idmiembro){
               Swal.fire({
                title: 'Quiere Activar este Miembro?',
                icon: 'Warning',
                showCancelButton: true,
                confirmButtonColor: '#3085d6',
                cancelButtonColor: '#d33',
                confirmButtonText: 'Aceptar',
                cancelButtonText: 'Cancelar',
                }).then((result) => {
                if (result.isConfirmed) {

                    let me = this;
                    axios.put('miembros/activar', {
                        'idmiembro' : idmiembro
                        })
                    .then(response =>{
                        me.listarMiembro(1, '', 'nombre');
                        Swal.fire(
                        'Activado!',
                        'El Miembro ha sido Activado.',
                        'Exito'
                    )
                    
                    })
                    .catch(error =>{
                        console.log(error.response);
                    });           


                }
                })  
            },
            desactivarMiembro(idmiembro){
               Swal.fire({
                title: 'Quiere Inactivar este Miembro?',
                icon: 'Warning',
                showCancelButton: true,
                confirmButtonColor: '#3085d6',
                cancelButtonColor: '#d33',
                confirmButtonText: 'Aceptar',
                cancelButtonText: 'Cancelar',
                }).then((result) => {
                if (result.isConfirmed) {

                    let me = this;
                    axios.put('miembros/desactivar', {
                        'idmiembro' : idmiembro
                        })
                    .then(response =>{
                        me.listarMiembro(1, '', 'nombre');
                        Swal.fire(
                        'Desactivado!',
                        'El Miembro ha sido Inactivado.',
                        'Exito'
                    )
                    
                    })
                    .catch(error =>{
                        console.log(error.response);
                    });           


                }
                })
            },
            selectMunicipio(iddepartamento){
                let me=this;
                var url= '/miembros/selectmunicipio?iddepartamento=' + iddepartamento;
                axios.get(url).then(function(response){
                    var respuesta = response.data;
                    
                    me.arrayMunicipio = respuesta.municipio;
                    //console.log(me.arrayMunicipio);
                })
            },
            selectDepartamento(){
                let me=this;
                var url= '/miembros/selectdepartamento';
                axios.get(url).then(function(response){
                    var respuesta = response.data;
                    
                    me.arrayDepartamento = respuesta.departamento;
                    //console.log(me.arrayGenero);
                })
            },
            selectEstadoCivil(){
                let me=this;
                var url= '/miembros/selectestadocivil';
                axios.get(url).then(function(response){
                    var respuesta = response.data;
                    
                    me.arrayEstadoCivil = respuesta.estadocivil;
                    //console.log(me.arrayGenero);
                })
            },
            selectGenero(){
                let me=this;
                var url= '/miembros/selectgenero';
                axios.get(url).then(function(response){
                    var respuesta = response.data;
                    
                    me.arrayGenero = respuesta.genero;
                    //console.log(me.arrayGenero);
                })
            },
            cambiarPagina(page, buscar, criterio){
                let me = this;
                me.pagination.current_page = page;
                me.listarMiembro(page,buscar, criterio);
            },
            cerrarmodal(){
                this.modal = 0;
                this.nombre = "";
                this.cui = "";
                this.fechanacimiento = '',
                this.lugarnacimiento = '',
                this.fechaconversion = '',
                this.lugarconversion = '',
                this.fechabautismoa = '',
                this.lugarbautismoa = '',
                this.fecharecepcion = '',
                this.lugarrecepcion = '',
                this.fechabautismoe = '',
                this.lugarbautismoe = '',
                this.fechapacto = '',
                this.profesion = '',
                this.oficio = '',
                this.foto = '';
                this.traslado = '';
                this.tituloModal = '';
            },
            validarMiembro(){
                this.errorMiembro = 0;
                this.mostrarError = [];
                if(!this.nombre) this.mostrarError.push('El nombre del miembro no puede estar vacio');
                if(!this.cui) this.mostrarError.push('El CUI del miembro no puede estar vacio');
                //if(!this.fechaconversion) this.mostrarError.push('La fecha del miembro no puede estar vacia');

                if(this.mostrarError.length) this.errorMiembro = 1;

                return this.errorMiembro;
            },
            abrirmodal(modelo, accion, data=[]){
                switch(modelo){
                    case "miembro":
                    {
                        switch(accion){
                            case "registrar":
                            {
                                this.modal = 1;
                                this.nombre = "";
                                this.cui = "";
                                this.tituloModal = "Registrar Miembro";
                                this.tipoAccion = 1;
                                break;          
                            }
                            case "actualizar":
                            {
                                this.modal = 1;
                                this.tituloModal = "Actualizar Miembro";
                                this.tipoAccion = 2;
                                this.nombre = data['nombre'];
                                this.cui = data['dpi'];

                                if(data.fechanacimiento == null){
                                     this.fechanacimiento = '';
                                }else{
                                    this.fechanacimiento = moment(data['fechanacimiento'],"YYYY-MM-DD").format('DD-MM-YYYY');
                                }

                                if(data.lugarnacimiento == null){
                                     this.lugarnacimiento = '';
                                }else{
                                    this.lugarnacimiento = data['lugarnacimiento'];
                                }
                                
                                

                                if(data.fechaconversion == null){
                                     this.fechaconversion = '';
                                }else{
                                    this.fechaconversion = moment(data['fechaconversion'],"YYYY-MM-DD").format('DD-MM-YYYY');
                                }

                                if(data.lugarconversion == null){
                                     this.lugarconversion = '';
                                }else{
                                    this.lugarconversion = data['lugarconversion'];
                                }
                                

                                if(data.fechabautismoa == null){
                                     this.fechabautismoa = '';
                                }else{
                                    this.fechabautismoa = moment(data['fechabautismoa'],"YYYY-MM-DD").format('DD-MM-YYYY');
                                }
                                if(data.lugarbautismoa == null){
                                     this.lugarbautismoa = '';
                                }else{
                                    this.lugarbautismoa = data['lugarbautismoa'];
                                }
                                

                                if(data.fecharecepcion == null){
                                     this.fecharecepcion = '';
                                }else{
                                    this.fecharecepcion = moment(data['fecharecepcion'],"YYYY-MM-DD").format('DD-MM-YYYY');
                                }
                                if(data.lugarrecepcion == null){
                                     this.lugarrecepcion = '';
                                }else{
                                    this.lugarrecepcion = data['lugarrecepcion'];
                                }
                                if(data.fechabautismoe == null){
                                     this.fechabautismoe = '';
                                }else{
                                    this.fechabautismoe = moment(data['fechabautismoe'],"YYYY-MM-DD").format('DD-MM-YYYY');
                                }
                                if(data.lugarbautismoe == null){
                                     this.lugarbautismoe = '';
                                }else{
                                     this.lugarbautismoe = data['lugarbautismoe'];
                                }

                                if(data.fechapacto == null){
                                     this.fechapacto = '';
                                }else{
                                     this.fechapacto = moment(data['fechapacto'],"YYYY-MM-DD").format('DD-MM-YYYY');
                                }
                               
                                this.idmunicipio = data['idmunicipio'];
                                this.idgenero = data['genero_idgenero'];
                                this.idestadocivil = data['idestadocivil'];
                                this.iddepartamento = data['iddepartamento'];
                                this.foto = data['foto'];
                                this.idmiembro = data['idmiembro'];

                                if(data.profesion == null){
                                     this.profesion = '';
                                }else{
                                     this.profesion = data['profesion'];
                                }
                                if(data.oficio == null){
                                     this.oficio = '';
                                }else{
                                     this.oficio = data['oficio'];
                                }
                                if(data.traslado == null){
                                     this.traslado = '';
                                }else{
                                     this.traslado = data['traslado'];
                                }
                                
                                break;
                            }
                        }
                        
                    }
                    
                }
                this.selectGenero();
                this.selectEstadoCivil();
                this.selectDepartamento();
            },
            abrirmodal2(data=[]){
                //this.mostrarImagen(data['foto']);
                this.modal2 = 1;
                this.nombre = data['nombre'];  
                this.tituloModal2 = this.nombre;       
                this.foto = data['foto'];                              
            },
            cerrarmodal2(){
                this.modal2 = 0;
                this.tituloModal2 = '';
            }
        },    
        mounted() {
            this.listarMiembro(1, this.buscar, this.criterio);
        }
    }
</script>
<style>
    .modal-content{
        width: 100% !important;
        position: absolute !important;
    }
    .modal{
        overflow-y: auto !important;
    }

    .mostrar{
        display: list-item !important;
        opacity: 1 !important;
        position: absolute !important;
        background-color: #3c29297a !important;
    }

    .modal2{
        overflow-y: auto !important;
    }

    .mostrar2{
        display: list-item !important;
        opacity: 1 !important;
        position: absolute !important;
        background-color: #3c29297a !important;
    }

    .div-error{
        display: flex;
        justify-content: center;
    }
</style>