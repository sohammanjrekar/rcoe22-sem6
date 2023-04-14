import React from 'react'

function AddProfile() {
  return (
    <>
      <div class="bckgrnd">
        <div class="container emp-profile pb-3">
          <form
            name="form"
            method="POST"
            action="."
            class="needs-validation"
            enctype="multipart/form-data"
          >
            <div class="row">
              <div class="col-md-4" id="all1">
                <h5 class="text-muted">Personal Informations:</h5>
                <br />

                <div class="d-flex justify-content-between">
                  <div class="m-1 mr-2">
                    <label class="text-muted">
                      <small>First Name:</small>
                    </label>
                    <input
                      type="email"
                      class="form-control"
                      id="exampleFormControlInput1"
                      placeholder="name@example.com"
                    />
                  </div>

                  <div class="m-1">
                    <label class="text-muted">
                      <small>Last Name:</small>
                    </label>
                    <input
                      type="email"
                      class="form-control"
                      id="exampleFormControlInput1"
                      placeholder="name@example.com"
                    />
                  </div>
                </div>

                <div class="ml-1">
                  <label class="text-muted">
                    <small>Phone Number:</small>
                  </label>
                  <input
                    type="email"
                    class="form-control"
                    id="exampleFormControlInput1"
                    placeholder="name@example.com"
                  />
                </div>
                <div class="ml-1">
                  <label class="text-muted">
                    <small>Parent/Gurdien Number:</small>
                  </label>
                  <input
                    type="email"
                    class="form-control"
                    id="exampleFormControlInput1"
                    placeholder="name@example.com"
                  />
                </div>
                <div class="m-1">
                  <label class="text-muted">
                    <small>Email:</small>
                  </label>
                  <input
                    type="email"
                    class="form-control"
                    id="exampleFormControlInput1"
                    placeholder="name@example.com"
                  />
                </div>
                <div class="m-1">
                  <label class="text-muted">
                    <small>Birth date:</small>
                  </label>
                  <input
                    type="email"
                    class="form-control"
                    id="exampleFormControlInput1"
                    placeholder="name@example.com"
                  />
                </div>
                <div class="m-1">
                  <label class="text-muted">
                    <small>Address:</small>
                  </label>
                  <input
                    type="email"
                    class="form-control"
                    id="exampleFormControlInput1"
                    placeholder="name@example.com"
                  />
                </div>
              </div>

              <div class="col-md-4" id="all2">
                <h5 class="text-muted">College Informations:</h5>
                <br />
                <div class="m-1">
                  <label class="text-muted">
                    <small>College:</small>
                  </label>
                  <input
                    type="email"
                    class="form-control"
                    id="exampleFormControlInput1"
                    placeholder="name@example.com"
                  />
                </div>
                <div class="m-1">
                  <label class="text-muted">
                    <small>Course:</small>
                  </label>
                  <input
                    type="email"
                    class="form-control"
                    id="exampleFormControlInput1"
                    placeholder="name@example.com"
                  />
                </div>
                <div class="m-1">
                  <label class="text-muted">
                    <small>Hostel Name:</small>
                  </label>
                  <input
                    type="email"
                    class="form-control"
                    id="exampleFormControlInput1"
                    placeholder="name@example.com"
                  />
                </div>
                <div class="m-1">
                  <label class="text-muted">
                    <small>AC/Non AC:</small>
                  </label>
                  <input
                    type="email"
                    class="form-control"
                    id="exampleFormControlInput1"
                    placeholder="name@example.com"
                  />
                </div>
                <div class="m-1">
                  <label class="text-muted">
                    <small>Shift:</small>
                  </label>
                  <input
                    type="email"
                    class="form-control"
                    id="exampleFormControlInput1"
                    placeholder="name@example.com"
                  />
                </div>
                <div class="m-1">
                  <label class="text-muted">
                    <small>Room No:</small>
                  </label>
                  <input
                    type="email"
                    class="form-control"
                    id="exampleFormControlInput1"
                    placeholder="name@example.com"
                  />
                </div>
              </div>

              <div class="col-md-4" id="all3">
                <h5 class="text-muted">Biometric Photo:</h5>
                <br />
                <div>
                  <div class="alert alert-warning">
                    <svg
                      width="1.0625em"
                      height="1em"
                      viewBox="0 0 17 16"
                      class="bi bi-exclamation-triangle"
                      fill="currentColor"
                      xmlns="http://www.w3.org/2000/svg"
                    >
                      <path
                        fill-rule="evenodd"
                        d="M7.938 2.016a.146.146 0 0 0-.054.057L1.027 13.74a.176.176 0 0 0-.002.183c.016.03.037.05.054.06.015.01.034.017.066.017h13.713a.12.12 0 0 0 .066-.017.163.163 0 0 0 .055-.06.176.176 0 0 0-.003-.183L8.12 2.073a.146.146 0 0 0-.054-.057A.13.13 0 0 0 8.002 2a.13.13 0 0 0-.064.016zm1.044-.45a1.13 1.13 0 0 0-1.96 0L.165 13.233c-.457.778.091 1.767.98 1.767h13.713c.889 0 1.438-.99.98-1.767L8.982 1.566z"
                      />
                      <path d="M7.002 12a1 1 0 1 1 2 0 1 1 0 0 1-2 0zM7.1 5.995a.905.905 0 1 1 1.8 0l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 5.995z" />
                    </svg>
                    <small>use only biometric pictures with .jpg format</small>
                  </div>
                  <img src="/18.jpg" alt="" width="100%" />
                </div>
                <div class="mt-3">
                  <div class="input-group mb-3">
                    <input
                      type="file"
                      class="form-control"
                      id="inputGroupFile02"
                    />
                    <label class="input-group-text" for="inputGroupFile02">
                      Upload
                    </label>
                  </div>
                </div>
              </div>

              <div class="spin-container" id="loading">
                <center>
                  <div>
                    <div class="spin" id="loader"></div>
                    <div class="spin" id="loader2"></div>
                    <div class="spin" id="loader3"></div>
                    <div class="spin" id="loader4"></div>
                    <span id="text">
                      <br />
                      Uploading...
                    </span>
                  </div>
                </center>
              </div>
            </div>
            <div class="mt-3" id="all4">
              <button
                type="submit"
                class="btn btn-outline-success m-1"
                onclick="loading()"
              >
                Save
              </button>
              <a href="{% url 'profiles'%}">
                <button type="button" class="btn btn-outline-danger m-1">
                  Cancel
                </button>
              </a>
              <p>
                *After Submit ,Please wait 1min for image encoding and reload
                page!!
              </p>
            </div>
          </form>
        </div>
      </div>
    </>
  )
}

export default AddProfile
