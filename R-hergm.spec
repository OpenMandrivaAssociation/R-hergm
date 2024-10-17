%global packname  hergm
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.3.10
Release:          1
Summary:          Hierarchical Exponential-Family Random Graph Models
Group:            Sciences/Mathematics
License:          GPL-3
URL:              https://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/hergm_1.3-10.tar.gz
Requires:         R-ergm R-snow 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-ergm R-snow

%description
The R package 'hergm' implements Hierarchical Exponential-Family Random
Graph Models (HERGMs), which can be used to model a wide range of
relational data (networks). 'hergm' implements both simulation and
Bayesian inference.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs

